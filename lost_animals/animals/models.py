from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator, RegexValidator

from accounts.models import ProfileUser
# Create your models here.


class Species(models.Model):
    species = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.species}"


class Animal(models.Model):
    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=300)
    description = models.TextField()

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    image_url = models.URLField()
    species = models.ForeignKey(Species, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.user.id}"