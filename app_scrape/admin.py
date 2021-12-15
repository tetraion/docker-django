from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Fav)
class FavAdmin(admin.ModelAdmin):
    pass