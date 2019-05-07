from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save

# Create your models here.

class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.URLField(default='https://www.lewesac.co.uk/wp-content/uploads/2017/12/default-avatar.jpg')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list

    def __str__(self):
        return f'{self.user}'

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = ProfileUser.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)