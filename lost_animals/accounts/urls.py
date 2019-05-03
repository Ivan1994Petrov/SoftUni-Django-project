from django.urls import path, re_path, include
from django.conf.urls import url
from . import views
from django.contrib.auth import login


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    re_path('^profile/(?P<pk>\d+)/$', views.UserProfileDetails.as_view(), name='user-details'),
    path('profile/', views.redirect_to_user_profile, name='user-redirect'),
    path('signup/', views.SignUp.as_view(), name='signup')

]
