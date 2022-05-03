from django.db import models


# Create your models here.
class Language(models.Model):
    """Class managing Language data"""

    name = models.CharField(max_length=100)
    frequency = models.IntegerField(default=0)


class Medium(models.Model):
    """Class managing Medium data"""

    name = models.TextField(default="")
    length_modifier_type = models.CharField(
        max_length=200, default="division", blank=True, null=True
    )
    length_modifier = models.IntegerField(default=1, blank=True, null=True)


class Material(models.Model):
    """Class managing Material data"""

    name = models.TextField(default="")
