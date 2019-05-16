from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.


def landing(request):
    respons = redirect('/animals/')
    return  respons
