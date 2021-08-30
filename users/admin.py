from django.contrib import admin
from .models import AppUser, Collection

# Register your models here.
admin.site.register(AppUser)
admin.site.register(Collection)
