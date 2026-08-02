from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

from .forms import UserRegisterForm, UserLoginForm, UserProfileForm
from .models import User


class UserLoginView(LoginView):
    """Авторизация пользователя по email и паролю"""
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('catalog:home')


class UserRegisterView(CreateView):
    """Регистрация пользователя + отправка приветственного письма"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        send_mail(
            subject='Добро пожаловать в Django Catalog!',
            message=f'Здравствуйте, {user.email}!\n\nСпасибо за регистрацию в нашем магазине.',
            from_email=settings.EMAIL_FROM,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return response


class UserProfileView(LoginRequiredMixin, UpdateView):
    """Редактирование профиля (доп. задание)"""
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Профиль успешно сохранён!')
        return super().form_valid(form)
