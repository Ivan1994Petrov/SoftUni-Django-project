
from django.urls import path, re_path, include

from . import views
from .decorators import check_recaptcha

urlpatterns = [
    path('profile/', views.redirect_user, name='profile'),
    re_path('profile/(?P<pk>\d+)/', views.UserDetail.as_view(), name='user-profile'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', check_recaptcha(views.SignUp.as_view()), name='signup'),


]
