from django.contrib import admin
from core.models import Medium, Material, Language

# Register your models here.
@admin.register(Language)
class CoDProfileAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"


@admin.register(Material)
class CoDProfileAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"


@admin.register(Medium)
class CoDProfileAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Medium"
        verbose_name_plural = "Mediums"
