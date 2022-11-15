from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()

    def __str__(self):
        return self.email