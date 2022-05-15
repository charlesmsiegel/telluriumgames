from django.db import models
from tc.models.character.human import Human

# Create your models here.
class Aberrant(Human):
    type = "aberrant"
