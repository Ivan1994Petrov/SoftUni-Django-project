from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from . import forms

from .models import ProfileUser

# Create your views here.
def has_access_to_modify(current_user, animal):
    if current_user.id == animal.user.id:
        return True
    return False

def redirect_user(request):
    url = f'/animals/'
    return HttpResponseRedirect(url)


class UserDetail(generic.DetailView):
    model = ProfileUser
    template_name = 'user_profile.html'
    context_object_name = 'user'

    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        return render(request, 'user_profile.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/animals/'
    template_name = 'signup.html'
    form = forms.UserForm()



