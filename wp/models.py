from django.db import models

# Create your models here.

class Mensage(models.Model):
    mensage = models.CharField(max_length=100)

    def __str__(self):
        return self.mensage
