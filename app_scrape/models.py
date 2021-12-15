from django.db import models

# Create your models here.
class Fav(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        null=False,
    )
    name = models.TextField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )
    price = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )
    url = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )
    def __str__(self):
        return self.name

    # def add_fav(self):
    #     self.save
