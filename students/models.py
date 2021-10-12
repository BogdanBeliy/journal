from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(default=0)
    group = models.PositiveSmallIntegerField(default=1)


