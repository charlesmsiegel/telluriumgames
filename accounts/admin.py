from accounts.models import CoDProfile, TCProfile, WoDProfile
from django.contrib import admin


# Register your models here.
@admin.register(CoDProfile)
class CoDProfileAdmin(admin.ModelAdmin):
    """ Class controlling the display of Profile in admin site """

    list_display = ("user", "storyteller")

@admin.register(WoDProfile)
class WoDProfileAdmin(admin.ModelAdmin):
    """ Class controlling the display of Profile in admin site """

    list_display = ("user", "storyteller")

@admin.register(TCProfile)
class TCProfileAdmin(admin.ModelAdmin):
    """ Class controlling the display of Profile in admin site """

    list_display = ("user", "storyteller")
