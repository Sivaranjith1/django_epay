from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD', required=True)
    email = forms.CharField(help_text='Required. email', required=True)

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2')