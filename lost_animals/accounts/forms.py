from django import forms
from django.contrib.auth.models import User
from .models import ProfileUser
from django.core.validators import RegexValidator, URLValidator, MinValueValidator
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    first_name = forms.CharField(required=True,
                           validators=[RegexValidator(r'^[A-Z][a-z]+$',
                                                      message="Name must start with capital latain letter, followed by latain small letters.")],
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control'
                               }
                           ))

    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    phone_number = forms.CharField(required=True,
                           validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")],
                           widget= forms.TextInput(
                               attrs= {
                                   'class': 'form-control'
                               }
                           ))
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'password', 'phone_number', 'email')

        def save(self, commit=True):
            user = super(UserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.name = self.cleaned_data['name']

            if commit:
                user.save()

            return user