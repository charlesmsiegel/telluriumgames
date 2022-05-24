from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, View

from wod.models.characters.human import Character, Human
from wod.models.characters.mage import Mage
from wod.models.items.human import Item
from wod.models.items.mage import Grimoire, Library, Wonder
from wod.models.locations.human import City, Location
from wod.models.locations.mage import Node


# Create your views here.
class CharacterIndexView(View):
    def get(self, request):
        context = self.get_context()
        return render(request, "wod/characters/index.html", context)

    def post(self, request):
        context = self.get_context()
        return render(request, "wod/characters/index.html", context)

    def get_context(self):
        characters = Character.objects.all().order_by("name")
        context = {}
        context["characters"] = characters
        return context


class LocationIndexView(View):
    def get(self, request):
        context = self.get_context()
        return render(request, "wod/locations/index.html", context)

    def post(self, request):
        context = self.get_context()
        return render(request, "wod/locations/index.html", context)

    def get_context(self):
        locations = Location.objects.all().order_by("name")
        context = {}
        context["locations"] = locations
        return context


class ItemIndexView(View):
    def get(self, request):
        context = self.get_context()
        return render(request, "wod/items/index.html", context)

    def post(self, request):
        context = self.get_context()
        return render(request, "wod/items/index.html", context)

    def get_context(self):
        items = Item.objects.all().order_by("name")
        context = {}
        context["items"] = items
        return context


class LocationDetailView(DetailView):
    model = Location
    template_name = "wod/locations/location/detail.html"


class CityDetailView(DetailView):
    model = City
    template_name = "wod/locations/city/detail.html"


class NodeDetailView(DetailView):
    model = Node
    template_name = "wod/locations/node/detail.html"


class GenericLocationDetailView(View):
    views = {
        "location": LocationDetailView,
        "city": CityDetailView,
        "node": NodeDetailView,
    }

    def get(self, request, *args, **kwargs):
        loc = Location.objects.get(pk=kwargs["pk"])
        if loc.type in self.views:
            return self.views[loc.type].as_view()(request, *args, **kwargs)
        return redirect("wod:location_index")


class ItemDetailView(DetailView):
    model = Item
    template_name = "wod/items/item/detail.html"


class WonderDetailView(DetailView):
    model = Wonder
    template_name = "wod/items/wonder/detail.html"


class GrimoireDetailView(DetailView):
    model = Grimoire
    template_name = "wod/items/grimoire/detail.html"


class LibraryDetailView(DetailView):
    model = Library
    template_name = "wod/items/library/detail.html"


class GenericItemDetailView(View):
    views = {
        "item": ItemDetailView,
        "wonder": WonderDetailView,
        "grimoire": GrimoireDetailView,
        "library": LibraryDetailView,
    }

    def get(self, request, *args, **kwargs):
        item = Item.objects.get(pk=kwargs["pk"])
        if item.type in self.views:
            return self.views[item.type].as_view()(request, *args, **kwargs)
        return redirect("wod:item_index")


class CharacterDetailView(DetailView):
    model = Character
    template_name = "wod/characters/character/detail.html"


class HumanDetailView(DetailView):
    model = Human
    template_name = "wod/characters/human/detail.html"


class MageDetailView(DetailView):
    model = Mage
    template_name = "wod/characters/mage/detail.html"


class GenericCharacterDetailView(View):
    character_views = {
        "character": CharacterDetailView,
        "human": HumanDetailView,
        "mage": MageDetailView,
    }

    def get(self, request, *args, **kwargs):
        char = Character.objects.get(pk=kwargs["pk"])
        if char.type in self.character_views:
            return self.character_views[char.type].as_view()(request, *args, **kwargs)
        return redirect("wod:characters_index")
