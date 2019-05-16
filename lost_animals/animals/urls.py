from django.urls import path, re_path

from . import views

# from reviews import views as review_views

urlpatterns = [
    path('', views.AnimalList.as_view(), name='animal'),
    path('species/', views.CreateSpecies.as_view(), name='species-add'),
    path('mine/', views.UserAnimalsList.as_view(), name='user-animals'),
    re_path('^details/(?P<pk>\d+)/$', views.AnimalDetail.as_view(), name='animal-detail'),
    re_path('^delete/(?P<pk>\d+)/$', views.AnimalDelete.as_view(), name='animal-delete'),
    re_path('^create/$', views.AnimalCreate.as_view(), name='animal-create'),
    re_path('^edit/(?P<pk>\d+)/$', views.AnimalsEdit.as_view(), name='animal-edit')

]

