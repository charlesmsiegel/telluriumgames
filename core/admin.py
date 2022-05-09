from core.models import Language, Material, Medium
from django.contrib import admin


# Register your models here.
@admin.register(Language)
class LanguageProfileAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"


@admin.register(Material)
class MaterialProfileAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"


@admin.register(Medium)
class MediumProfileAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Medium"
        verbose_name_plural = "Mediums"
