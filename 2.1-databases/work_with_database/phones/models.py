from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)
