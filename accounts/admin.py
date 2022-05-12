from django.contrib import admin

from accounts.models import CoDProfile, TCProfile, WoDProfile


# Register your models here.
@admin.register(CoDProfile)
class CoDProfileAdmin(admin.ModelAdmin):
    """ Class controlling the display of Profile in admin site """

    list_display = ("user", "storyteller")

    class Meta:
        verbose_name = "CoD Profile"
        verbose_name_plural = "CoD Profiles"


@admin.register(WoDProfile)
class WoDProfileAdmin(admin.ModelAdmin):
    """ Class controlling the display of Profile in admin site """

    list_display = ("user", "storyteller")

    class Meta:
        verbose_name = "WoD Profile"
        verbose_name_plural = "WoD Profiles"


@admin.register(TCProfile)
class TCProfileAdmin(admin.ModelAdmin):
    """ Class controlling the display of Profile in admin site """

    list_display = ("user", "storyteller")

    class Meta:
        verbose_name = "TC Profile"
        verbose_name_plural = "TC Profiles"
