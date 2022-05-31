from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, View

from wod.models.characters.human import Character, Human
from wod.models.characters.mage import Mage
from wod.models.items.human import Item
from wod.models.items.mage import Grimoire, Library, Wonder
from wod.models.locations.human import City, Location
from wod.models.locations.mage import Node, NodeMeritFlawRating, NodeResonanceRating


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


class NodeDetailView(View):
    def get(self, request, *args, **kwargs):
        node = Node.objects.get(pk=kwargs["pk"])
        context = self.get_context(node)
        return render(request, "wod/locations/node/detail.html", context)
    
    def get_context(self, node):
        return {
            "object": node,
            "resonance": NodeResonanceRating.objects.filter(node=node).order_by("resonance__name"),
            "merits_and_flaws": NodeMeritFlawRating.objects.filter(node=node).order_by("mf__name"),
        }


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


class RandomLocationView(View):
    locs = {
        "node": Node,
    }

    def post(self, request):
        location = self.locs[request.POST['location_type']].objects.create(name=request.POST['node_name'])
        if request.POST['node_rank'] == None:
            rank = None
        else:
            rank = int(request.POST['node_rank'])
        location.random(rank=rank)
        location.save()
        return redirect(location.get_absolute_url())
    
    def get(self, request):
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

class GrimoireDetailView(View):
    def get(self, request, *args, **kwargs):
        grimoire = Grimoire.objects.get(pk=kwargs["pk"])
        context = self.get_context(grimoire)
        return render(request, "wod/items/grimoire/detail.html", context)
    
    def get_context(self, node):
        if node.faction.parent is not None:
            if node.faction.parent.parent is not None:
                s = f"{node.faction.parent} ({node.faction})"
            else:
                s = f"{node.faction}"
        return {
            "object": node,
            "paradigms": "<br>".join([str(x) for x in node.paradigms.all()]),
            "practices": "<br>".join([str(x) for x in node.practices.all()]),
            "instruments": "<br>".join([str(x) for x in node.instruments.all()]),
            "abilities": "<br>".join([x.replace("_", " ").title() for x in node.abilities]),
            "spheres": "<br>".join([x.replace("_", " ").title() for x in node.spheres]),
            "rotes": "<br>".join([str(x) for x in node.rotes.all()]),
            "date_written": node.date_written,
            "faction": s,
        }


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

class RandomItemView(View):
    items = {
        "grimoire": Grimoire,
    }

    def post(self, request):
        item = self.items[request.POST['item_type']].objects.create(name=request.POST['item_name'])
        if request.POST['item_rank'] == None:
            rank = None
        else:
            rank = int(request.POST['item_rank'])
        item.random(rank=rank)
        item.save()
        return redirect(item.get_absolute_url())
    
    def get(self, request):
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
