from django.db import models
from polymorphic.models import PolymorphicModel

from accounts.models import WoDProfile


# Create your models here.
class Character(PolymorphicModel):
    type = "character"

    name = models.CharField(max_length=100, unique=True)
    player = models.ForeignKey(
        WoDProfile, on_delete=models.CASCADE, related_name="characters"
    )
