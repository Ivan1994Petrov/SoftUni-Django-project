from django.shortcuts import render
from animals.models import Animal
from .filters import AnimalFilter
# Create your views here.


def search(request):
    animal_list = Animal.objects.all()
    animal_filter = AnimalFilter(request.GET, queryset=animal_list)
    return render(request, 'animal_list.html', {'filter': animal_filter})

