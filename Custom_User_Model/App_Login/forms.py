from django import forms
from django import forms
from App_Login.models import User

from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={

        'type' : 'date'

    }))

    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={

        'type': 'password'
    }))

    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(attrs={

        'type': 'password'
    }))

    class Meta:

        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'address', 'country', 'zipcode','password1', 'password2')