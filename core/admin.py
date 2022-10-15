from tabnanny import verbose

from django.contrib import admin
from pyparsing import Char

from core.models import (
    Book,
    BookReference,
    CharacterModel,
    ItemModel,
    Language,
    LocationModel,
    Material,
    Medium,
    NewsItem,
)


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


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


admin.site.register(NewsItem)
admin.site.register(CharacterModel)
admin.site.register(ItemModel)
admin.site.register(LocationModel)
admin.site.register(BookReference)
