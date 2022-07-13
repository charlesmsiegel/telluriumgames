from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wod_st = models.BooleanField(default=False)
    cod_st = models.BooleanField(default=False)
    tc_st = models.BooleanField(default=False)
    exalted_st = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
