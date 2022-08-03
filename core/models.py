from django.db import models


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
