from django import forms

from .models import Animal, Species, FoundOrLost


class SpeciesForm(forms.ModelForm):
    species = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-contol'
        }
    ))

    class Meta:
        model = Species
        fields = ('species',)


class CreateAnimalForm(forms.ModelForm):

    location = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    phone_number = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    description = forms.CharField(required=True ,widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

    species = forms.ModelChoiceField(queryset=Species.objects.all(),
                                      widget=forms.Select(
                                          attrs={
                                              'class': 'form-control'
                                          }
                                      ))

    found_or_lost = forms.ModelChoiceField(queryset=FoundOrLost.objects.all(),
                                           widget=forms.Select(
                                               attrs={
                                                   'class': 'form-control'
                                               }
                                           ))

    class Meta:
        model = Animal
        fields = ('id', 'location', 'phone_number', 'description', 'species', 'uploaded_image', 'date', 'found_or_lost')