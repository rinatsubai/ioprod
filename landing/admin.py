from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Artist, Release, Genre)
class PersonAdmin(admin.ModelAdmin):
    pass