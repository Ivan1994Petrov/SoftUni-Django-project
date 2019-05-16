from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from . import forms

from .models import ProfileUser

# Create your views here.


def redirect_user(request):
    url = f'/animals/'
    return HttpResponseRedirect(url)


class UserDetail(generic.DetailView):
    model = ProfileUser
    template_name = 'user_profile.html'
    context_object_name = 'user'


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/animals/'
    template_name = 'signup.html'
    form = forms.UserForm()



