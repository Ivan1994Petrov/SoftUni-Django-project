from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Animal, Species
from .forms import CreateAnimalForm, SpeciesForm

from accounts.models import ProfileUser



def has_access_to_modify(current_user, animal):
    if current_user.is_superuser:
        return True
    elif current_user.id == animal.user.id:
        return True
    return False


class AnimalList(generic.ListView):
    model = Animal
    template_name = 'animals_list.html'
    context_object_name = 'animal'
    paginate_by = 6


class UserAnimalsList(LoginRequiredMixin, generic.ListView):
    model = Animal
    template_name = 'animals_list.html'
    context_object_name = 'animal'


    def get_queryset(self):
        user_id = int(self.request.user.id)

        try:
            user = ProfileUser.objects.all().filter(user__pk=user_id)[0]
            animals = Animal.objects.all().filter(user = user.pk)
            return animals
        except:
            return []


class AnimalDetail(LoginRequiredMixin, generic.DetailView):
    model = Animal
    login_url = '/accounts/login/'
    context_object_name = 'animal'
    template_name = 'animal_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AnimalDetail, self).get_context_data(**kwargs)
        owner = context['object'].user
        current_user = self.request.user
        if has_access_to_modify(current_user, owner):
            context['is_user_furniture'] = True
            return context
        context['is_user_furniture'] = False
        return context

    def post(self,request, pk):
        url = f'/animal/details/{self.get_object().id}/'
        post_values = request.POST.copy()
        post_values['animal'] = self.get_object()
        return HttpResponseRedirect(url)


class AnimalDelete(LoginRequiredMixin, generic.DeleteView):
    model = Animal
    login_url = 'accounts/login/'
    context_object_name = 'animal'

    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        return render(request, 'animal_delete.html', {'animal': self.get_object()})

    def post(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        animal = self.get_object()
        animal.delete()
        return HttpResponseRedirect('/animals/')


class AnimalCreate(LoginRequiredMixin, generic.CreateView):
    model = Animal
    template_name = 'animal_create.html'
    form_class = CreateAnimalForm
    success_url = '/animals/'

    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)


class AnimalsEdit(generic.edit.UpdateView):
    model = Animal
    form_class = CreateAnimalForm
    template_name = 'animal_create.html'
    success_url = '/animals/'

    def form_valid(self, form):
        user = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)

    # def get_object(self, queryset=None):
    #     instance = Animal.objects.get(pk=self.us)

    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        instance = Animal.objects.get(pk=pk)
        instance = Animal.objects.get(pk=pk)
        form = CreateAnimalForm(request.POST or None, instance=instance)
        return render(request, 'animal_create.html', {'form': form})


class CreateSpecies(generic.CreateView):
    model = Species
    template_name = 'species_create.html'
    form_class = SpeciesForm
    success_url = '/animals/'


