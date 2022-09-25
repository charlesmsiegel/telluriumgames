from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel

from game.models.chronicle import Chronicle


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
        return f"<i>{self.book}</i> p. {self.page}"


def filepath(instance, filename):
    s = str(instance.__class__).split(" ")[-1][:-1][1:-1]
    s = "/".join([x for x in s.split(".") if x != "models"])
    s += "/" + instance.name
    s += "." + filename.split(".")[-1]
    return s


class Model(PolymorphicModel):
    type = "model"

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    status_keys = ["Un", "Sub", "App", "Ret", "Dec", "Ran", "Fre"]
    statuses = [
        "Unfinished",
        "Submitted",
        "Approved",
        "Retired",
        "Deceased",
        "Random",
        "Freeform",
    ]
    status = models.CharField(
        max_length=3, choices=zip(status_keys, statuses), default="Un"
    )
    display = models.BooleanField(default=True)
    description = models.TextField(default="")
    sources = models.ManyToManyField(BookReference, blank=True)
    chronicle = models.ForeignKey(
        Chronicle, blank=True, null=True, on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to=filepath, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def get_gameline(self):
        s = str(self.__class__).split(" ")[-1][:-1][1:-1].split(".")[0]
        if s == "wod":
            return "World of Darkness"
        if s == "cod":
            return "Chronicles of Darkness"
        if s == "tc":
            return "Trinity Continuum"
        return str(self.__class__).split(" ")[-1][:-1][1:-1].split(".")[0].title()

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


class CharacterModel(Model):
    pass

class LocationModel(Model):
    pass

class ItemModel(Model):
    pass

class NewsItem(models.Model):
    title = models.CharField(default="", max_length=100)
    content = models.TextField(default="")
    date = models.DateField()
