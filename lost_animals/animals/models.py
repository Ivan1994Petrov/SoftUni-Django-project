from django.db import models
from django.core.validators import RegexValidator

from accounts.models import ProfileUser

import datetime
# Create your models here.


class Species(models.Model):
    species = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.species}"


class FoundOrLost(models.Model):
    found_or_lost = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.found_or_lost}'


class Animal(models.Model):
    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=300)
    description = models.TextField()

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    species = models.ForeignKey(Species, on_delete=models.CASCADE, blank=True)
    found_or_lost = models.ForeignKey(FoundOrLost, on_delete=models.CASCADE, blank=True, null=True)
    uploaded_image = models.ImageField(upload_to='media/',null=True, blank=True)

    date = models.DateField(default=datetime.date.today, blank=True)

    def __str__(self):
        return f"{self.id}"