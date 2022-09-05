from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel

from game.models import Chronicle


# Create your models here.
class Language(models.Model):
    """Class managing Language data"""

    name = models.CharField(max_length=100)
    frequency = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("language", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("update_language", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name}"


class Medium(models.Model):
    """Class managing Medium data"""

    name = models.TextField(default="")
    length_modifier_type = models.CharField(
        max_length=1, default="/", blank=True, null=True
    )
    length_modifier = models.IntegerField(default=1, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("medium", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("update_medium", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name}"


class Material(models.Model):
    """Class managing Material data"""

    name = models.TextField(default="")

    def get_absolute_url(self):
        return reverse("material", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("update_material", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name}"


class Noun(models.Model):
    name = models.TextField(default="")

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.TextField(default="")

    def get_absolute_url(self):
        return reverse("book", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("update_book", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class BookReference(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.book} p. {self.page}"


class Model(PolymorphicModel):
    type = "model"

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    status_keys = ["Un", "Sub", "App", "Ret", "Dec", "Ran"]
    statuses = ["Unfinished", "Submitted", "Approved", "Retired", "Deceased", "Random"]
    status = models.CharField(
        max_length=3, choices=zip(status_keys, statuses), default="Un"
    )
    display = models.BooleanField(default=True)
    description = models.TextField(default="")
    sources = models.ManyToManyField(BookReference, blank=True)
    chronicle = models.ForeignKey(
        Chronicle, blank=True, null=True, on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="uploads/", blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def has_name(self):
        return self.name != ""

    def set_name(self, name):
        self.name = name
        return True

    def has_description(self):
        return self.description != ""

    def set_description(self, description):
        self.description = description
        return True

    def has_owner(self):
        return self.owner is not None

    def set_owner(self, owner):
        self.owner = owner
        return True

    def update_status(self, status):
        self.status = status
        return True

    def toggle_display(self):
        self.display = not self.display

    def has_source(self):
        return self.sources.count() > 0

    def add_source(self, book_title, page_number):
        book = Book.objects.get_or_create(name=book_title)[0]
        bookref = BookReference.objects.get_or_create(book=book, page=page_number)[0]
        self.sources.add(bookref)
        return self


class NewsItem(models.Model):
    title = models.CharField(default="", max_length=100)
    content = models.TextField(default="")
    date = models.DateField()
