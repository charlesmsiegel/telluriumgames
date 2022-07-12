from django.contrib import admin

from core.models import Language, Material, Medium


# Register your models here.
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"


@admin.register(Medium)
class MediumAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Medium"
        verbose_name_plural = "Mediums"
