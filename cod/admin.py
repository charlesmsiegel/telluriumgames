from cod.models import Merit, Mortal, Specialty
from django.contrib import admin

# Register your models here.
@admin.register(Mortal)
class CoDProfileAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Mortal"
        verbose_name_plural = "Mortals"


@admin.register(Specialty)
class CoDProfileAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"


@admin.register(Merit)
class CoDProfileAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Merit"
        verbose_name_plural = "Merits"
