from django.db import models


# Create your models here.
class Instrument(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Practice(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abilities = models.JSONField(default=list)
    instruments = models.ManyToManyField(Instrument, blank=True)

    def __str__(self):
        return self.name


class Paradigm(models.Model):
    name = models.CharField(max_length=100, unique=True)
    practices = models.ManyToManyField(Practice, blank=True)

    def __str__(self):
        return self.name
