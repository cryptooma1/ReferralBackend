from django.db import models

# Create your models here.

class NomaUser(models.Model):
    location = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, unique=True)
    wallet = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'NomaUser'
        verbose_name_plural = 'NomaUsers'
        ordering = ['name']