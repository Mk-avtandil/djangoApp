from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control'}))

