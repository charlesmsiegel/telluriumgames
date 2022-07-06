from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class CoDProfile(models.Model):
    """Class extending the User model to add additional fields."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="cod_profile"
    )
    storyteller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def update_codprofile_signal(sender, instance, created, **kwargs):
    if created:
        CoDProfile.objects.create(user=instance)
    instance.cod_profile.save()


class WoDProfile(models.Model):
    """Class extending the User model to add additional fields."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="wod_profile"
    )
    storyteller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def update_wodprofile_signal(sender, instance, created, **kwargs):
    if created:
        WoDProfile.objects.create(user=instance)
    instance.wod_profile.save()


class TCProfile(models.Model):
    """Class extending the User model to add additional fields."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="tc_profile"
    )
    storyteller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def update_tcprofile_signal(sender, instance, created, **kwargs):
    if created:
        TCProfile.objects.create(user=instance)
    instance.tc_profile.save()


class ExaltedProfile(models.Model):
    """Class extending the User model to add additional fields."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="exalted_profile"
    )
    storyteller = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def update_exaltedprofile_signal(sender, instance, created, **kwargs):
    if created:
        ExaltedProfile.objects.create(user=instance)
    instance.exalted_profile.save()
