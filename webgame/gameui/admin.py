from django.contrib import admin
from .models import User, Pet, Egg, UserProfile

# Register your models here.
admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Egg)
admin.site.register(UserProfile)