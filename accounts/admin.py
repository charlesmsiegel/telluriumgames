from django.contrib import admin

from accounts.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Class controlling the display of Profile in admin site """

    list_display = ("user", "storyteller")
