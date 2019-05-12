import django_filters
from django import forms


from animals.models import Animal, Species


class AnimalFilter(django_filters.FilterSet):
    date = django_filters.NumberFilter(lookup_expr='year__gt')

    class Meta:
        model = Animal
        fields = ['location', 'species', 'found_or_lost', 'date']