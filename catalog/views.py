from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import models                                          # ← добавили импорт
from catalog.models import Product
from catalog.forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'page_obj'
    paginate_by = 6

    def get_queryset(self):                                           # ← добавили метод
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            # Опубликованные товары + свои черновики
            return queryset.filter(
                models.Q(is_published=True) | models.Q(owner=self.request.user)
            )
        return queryset.filter(is_published=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        return user == product.owner or user.groups.filter(name='Модератор продуктов').exists()

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        return user == product.owner or user.groups.filter(name='Модератор продуктов').exists()


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
