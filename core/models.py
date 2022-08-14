from django.db import models
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel

# Create your models here.
class Language(models.Model):
    """Class managing Language data"""

    name = models.CharField(max_length=100)
    frequency = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Medium(models.Model):
    """Class managing Medium data"""

    name = models.TextField(default="")
    length_modifier_type = models.CharField(
        max_length=1, default="/", blank=True, null=True
    )
    length_modifier = models.IntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Material(models.Model):
    """Class managing Material data"""

    name = models.TextField(default="")

    def __str__(self):
        return f"{self.name}"


class Noun(models.Model):
    name = models.TextField(default="")

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.TextField(default="")

    def __str__(self):
        return self.name

class BookReference(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page = models.IntegerField(default=0)

class Model(PolymorphicModel):
    type = "model"
    
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    status_keys = ["Un", "Sub", "App", "Ret", "Dec"]
    statuses = ["Unfinished", "Submitted", "Approved", "Retired", "Deceased"]
    status = models.CharField(max_length=3, choices=zip(status_keys, statuses), default="Un")
    display = models.BooleanField(default=True)
    description = models.TextField(default="")
    sources = models.ForeignKey(BookReference, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
