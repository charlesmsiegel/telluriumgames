from collections import defaultdict

from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, View

from core.utils import level_name, tree_sort
from wod.forms import RandomCharacterForm
from wod.models.characters.human import Character, Human, MeritFlawRating
from wod.models.characters.mage import Mage, ResRating
from wod.models.characters.werewolf import Werewolf
from wod.models.items.human import Item
from wod.models.items.mage import Grimoire, Library, Wonder
from wod.models.locations.human import City, Location
from wod.models.locations.mage import (
    Chantry,
    Node,
    NodeMeritFlawRating,
    NodeResonanceRating,
)


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
        context["form"] = RandomCharacterForm
        return context


def load_character_types(request):
    print("WAAAAAAAAAAAAAAAAAAAAA")
    characters = {
        "werewolf": ["werewolf"],
        "mage": ["mage"],
    }
    gameline = request.GET.get("gameline")
    character_types = characters[gameline]
    return render(
        request,
        "wod/characters/load_character_dropdown_list.html",
        {"character_types": character_types},
    )


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

        L1 = []
        L2 = []
        for x in Location.objects.filter(parent=None).order_by("name"):
            L1.extend([level_name(y) for y in tree_sort(x)])
            L2.extend(tree_sort(x))

        context["names_dict"] = dict(zip(L1, L2))
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
            "resonance": NodeResonanceRating.objects.filter(node=node).order_by(
                "resonance__name"
            ),
            "merits_and_flaws": NodeMeritFlawRating.objects.filter(node=node).order_by(
                "mf__name"
            ),
        }


class ChantryDetailView(View):
    def get(self, request, *args, **kwargs):
        chantry = Chantry.objects.get(pk=kwargs["pk"])
        context = self.get_context(chantry)
        return render(request, "wod/locations/chantry/detail.html", context)

    def get_context(self, chantry):
        factions = []
        f = chantry.faction
        while f is not None:
            factions.append(f.name)
            f = f.parent
        factions.reverse()
        factions = "/".join(factions)
        return {
            "factions": factions,
            "object": chantry,
        }


class GenericLocationDetailView(View):
    views = {
        "location": LocationDetailView,
        "city": CityDetailView,
        "node": NodeDetailView,
        "chantry": ChantryDetailView,
    }

    def get(self, request, *args, **kwargs):
        loc = Location.objects.get(pk=kwargs["pk"])
        if loc.type in self.views:
            return self.views[loc.type].as_view()(request, *args, **kwargs)
        return redirect("wod:location_index")


class RandomLocationView(View):
    locs = {
        "node": Node,
        "chantry": Chantry,
    }

    def post(self, request):
        location = self.locs[request.POST["location_type"]].objects.create(
            name=request.POST["name"]
        )
        if request.POST["rank"] is None:
            rank = None
        else:
            rank = int(request.POST["rank"])
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


class GrimoireDetailView(View):
    def get(self, request, *args, **kwargs):
        grimoire = Grimoire.objects.get(pk=kwargs["pk"])
        context = self.get_context(grimoire)
        return render(request, "wod/items/grimoire/detail.html", context)

    def get_context(self, grimoire):
        if grimoire.faction is not None:
            if grimoire.faction.parent is not None:
                if grimoire.faction.parent.parent is not None:
                    s = f"{grimoire.faction.parent} ({grimoire.faction})"
                else:
                    s = f"{grimoire.faction}"
            else:
                s = ""
        else:
            s = ""
        return {
            "object": grimoire,
            "paradigms": "<br>".join([str(x) for x in grimoire.paradigms.all()]),
            "practices": "<br>".join([str(x) for x in grimoire.practices.all()]),
            "instruments": "<br>".join([str(x) for x in grimoire.instruments.all()]),
            "abilities": "<br>".join(
                [x.replace("_", " ").title() for x in grimoire.abilities]
            ),
            "spheres": "<br>".join(
                [x.replace("_", " ").title() for x in grimoire.spheres]
            ),
            "rotes": "<br>".join([str(x) for x in grimoire.rotes.all()]),
            "date_written": grimoire.date_written,
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
        item = self.items[request.POST["item_type"]].objects.create(
            name=request.POST["item_name"]
        )
        if request.POST["item_rank"] is None:
            rank = None
        else:
            rank = int(request.POST["item_rank"])
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


class WerewolfDetailView(View):
    def get(self, request, *args, **kwargs):
        werewolf = Werewolf.objects.get(pk=kwargs["pk"])
        context = self.get_context(werewolf)
        return render(request, "wod/characters/werewolf/detail.html", context)

    def get_context(self, werewolf):
        context = {"object": werewolf}
        specialties = {}
        for attribute in werewolf.get_attributes():
            specialties[attribute] = ", ".join(
                [x.name for x in werewolf.specialties.filter(stat=attribute)]
            )
        for ability in werewolf.get_abilities():
            specialties[ability] = ", ".join(
                [x.name for x in werewolf.specialties.filter(stat=ability)]
            )
        for key, value in specialties.items():
            context[f"{key}_spec"] = value

        context["merits_and_flaws"] = MeritFlawRating.objects.order_by(
            "mf__name"
        ).filter(character=werewolf)
        all_gifts = list(context["object"].gifts.all())
        row_length = 3
        all_gifts = [
            all_gifts[i : i + row_length] for i in range(0, len(all_gifts), row_length)
        ]
        context["gifts"] = all_gifts

        all_rites = list(context["object"].rites_known.all())
        row_length = 3
        all_rites = [
            all_rites[i : i + row_length] for i in range(0, len(all_rites), row_length)
        ]
        context["rites"] = all_rites
        context["rank_name"] = werewolf.rank_names[werewolf.rank]
        return context


class MageDetailView(View):
    def get(self, request, *args, **kwargs):
        mage = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(mage)
        return render(request, "wod/characters/mage/detail.html", context)

    def get_context(self, mage):
        context = {"object": mage}
        specialties = {}
        for attribute in mage.get_attributes():
            specialties[attribute] = ", ".join(
                [x.name for x in mage.specialties.filter(stat=attribute)]
            )
        for ability in mage.get_abilities():
            specialties[ability] = ", ".join(
                [x.name for x in mage.specialties.filter(stat=ability)]
            )
        for sphere in mage.get_spheres():
            specialties[sphere] = ", ".join(
                [x.name for x in mage.specialties.filter(stat=sphere)]
            )
        for key, value in specialties.items():
            context[f"{key}_spec"] = value

        context["resonance"] = ResRating.objects.filter(mage=mage).order_by(
            "resonance__name"
        )
        context["merits_and_flaws"] = MeritFlawRating.objects.order_by(
            "mf__name"
        ).filter(character=mage)
        all_rotes = list(context["object"].rotes.all())
        row_length = 2
        all_rotes = [
            all_rotes[i : i + row_length] for i in range(0, len(all_rotes), row_length)
        ]
        context["rotes"] = all_rotes
        return context


class GenericCharacterDetailView(View):
    character_views = {
        "character": CharacterDetailView,
        "human": HumanDetailView,
        "garou": WerewolfDetailView,
        "mage": MageDetailView,
    }

    def get(self, request, *args, **kwargs):
        char = Character.objects.get(pk=kwargs["pk"])
        if char.type in self.character_views:
            return self.character_views[char.type].as_view()(request, *args, **kwargs)
        return redirect("wod:characters_index")


class RandomCharacterView(View):
    chars = {
        "werewolf": Werewolf,
        "mage": Mage,
    }

    def post(self, request, *args, **kwargs):
        char = self.chars[request.POST["character_type"]].objects.create(
            name=request.POST["character_name"], player=request.user.wod_profile
        )
        try:
            freebies = int(request.POST["freebies"])
        except ValueError:
            freebies = 15
        try:
            xp = int(request.POST["xp"])
        except ValueError:
            xp = 0
        xp = max(xp, 0)
        freebies = max(freebies, 0)
        char.random(freebies=freebies, xp=xp)
        char.save()
        return redirect(char.get_absolute_url())

    def get(self, request):
        return redirect("wod:characters_index")
