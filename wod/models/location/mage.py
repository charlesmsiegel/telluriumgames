from django.db import models

from wod.models.location.human import Location


# Create your models here.
class Node(Location):
    type = "node"
