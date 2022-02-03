from django.db import models

# Create your models here.

class Person(models.Model):
    image = models.ImageField("Rasm", upload_to='imgs/')
    name = models.CharField(max_length=100)
    description = models.TextField()


