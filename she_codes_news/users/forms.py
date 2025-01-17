from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required= False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required= False, help_text='Optional.')
    email = forms.EmailField(max_length=30, help_text='Email required.')

    class Meta:
        model = CustomUser
        fields = ['username', 'email',]