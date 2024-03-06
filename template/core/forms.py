from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class': "form-control",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password',
            'class': "form-control",
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class': "form-control",
        }
    ))

    email = forms.CharField(
        help_text="We'll never share your email with anyone else.",
        max_length=50,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your email address',
            'aria-describedby': "email_id_help",
            'class': "form-control",
        }
    ))
    
    password1 = forms.CharField(
        help_text="Password must contain at least 8 characters and be a mixture of numbers and letters.",
        max_length=50,
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password',            
            'class': "form-control",
    }))

    password2 = forms.CharField(
        label = "Repeat password",
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat password',
            'class': "form-control",
    }))
