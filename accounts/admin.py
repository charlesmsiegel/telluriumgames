from django.contrib import admin

from accounts.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "wod_st", "cod_st", "tc_st", "exalted_st")
