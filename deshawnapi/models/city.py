from django.db import models #base class from Django stdlib


class City(models.Model): #must inherit from this base class
    name = models.CharField(max_length=155) #define all non "id" fields, no need for ID it auto adds it from Django
