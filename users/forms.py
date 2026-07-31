from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'phone', 'country')
