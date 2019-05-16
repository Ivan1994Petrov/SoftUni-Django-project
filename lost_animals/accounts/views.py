from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.views import generic
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# # Create your views here.
#
# def redirect_to_user_profile(request):
#     url = f'/accounts/profile/{request.user.id}/'
#     return HttpResponseRedirect(redirect_to=url)
#
# class UserProfileDetails(generic.DetailView):
#     model = User
#     template_name = 'user_profile.html'
#     context_object_name = 'user'
#
#
# class SignUp(generic.CreateView):
#     model = User
#     form_class = UserCreationForm
#     template_name = 'signup.html'
#     success_url = '/accounts/login/'


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



