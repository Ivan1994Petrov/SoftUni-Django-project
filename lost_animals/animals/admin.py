from django.contrib import admin

from .models import Species, Animal, FoundOrLost

admin.site.register(Species)
admin.site.register(Animal)
admin.site.register(FoundOrLost)