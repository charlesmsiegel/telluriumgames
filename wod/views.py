from collections import defaultdict, namedtuple

from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DetailView, View

from core.utils import level_name, tree_sort
from wod.forms import MageForm, RandomCharacterForm
from wod.models.characters.human import (
    Archetype,
    Character,
    Group,
    Human,
    MeritFlaw,
    MeritFlawRating,
    Specialty,
)
from wod.models.characters.mage import (
    Cabal,
    Instrument,
    Mage,
    MageFaction,
    Paradigm,
    Practice,
    Resonance,
    ResRating,
    Rote,
)
from wod.models.characters.mage.utils import PRIMARY_ABILITIES
from wod.models.characters.werewolf import (
    Camp,
    Gift,
    Pack,
    RenownIncident,
    Rite,
    Totem,
    Tribe,
    Werewolf,
)
from wod.models.locations.werewolf import Caern
from wod.models.items.human import Item
from wod.models.items.mage import Grimoire, Library, Wonder
from wod.models.items.werewolf import Fetish
from wod.models.locations.human import City, Location
from wod.models.locations.mage import (
    Chantry,
    Node,
    NodeMeritFlaw,
    NodeMeritFlawRating,
    NodeResonanceRating,
)

EmptyRote = namedtuple("EmptyRote", ["name", "spheres"])
empty_rote = EmptyRote("", "")


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
        context["groups"] = Group.objects.all().order_by("name")
        return context


def load_character_types(request):
    characters = {
        "werewolf": ["werewolf", "pack"],
        "mage": ["mage", "cabal"],
    }
    gameline = request.GET.get("gameline")
    character_types = characters[gameline]
    return render(
        request,
        "wod/characters/load_character_dropdown_list.html",
        {"character_types": character_types},
    )


def load_factions(request):
    affiliation_id = request.GET.get("affiliation")
    factions = MageFaction.objects.filter(parent=affiliation_id).order_by("name")
    return render(
        request,
        "wod/characters/mage/load_faction_dropdown_list.html",
        {"factions": factions},
    )


def load_subfactions(request):
    faction_id = request.GET.get("faction")
    subfactions = MageFaction.objects.filter(parent=faction_id).order_by("name")
    return render(
        request,
        "wod/characters/mage/load_subfaction_dropdown_list.html",
        {"subfactions": subfactions},
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


class LocationCreateView(CreateView):
    model = Location
    fields = "__all__"
    template_name = "wod/locations/location/create.html"


class CityDetailView(DetailView):
    model = City
    template_name = "wod/locations/city/detail.html"


class CityCreateView(CreateView):
    model = City
    fields = "__all__"
    template_name = "wod/locations/city/create.html"


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


class NodeCreateView(CreateView):
    model = Node
    fields = "__all__"
    template_name = "wod/locations/node/create.html"


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


class ChantryCreateView(CreateView):
    model = Chantry
    fields = "__all__"
    template_name = "wod/locations/chantry/create.html"


class CaernDetailView(DetailView):
    model = Caern
    template_name = "wod/locations/caern/detail.html"


class GenericLocationDetailView(View):
    views = {
        "location": LocationDetailView,
        "city": CityDetailView,
        "node": NodeDetailView,
        "chantry": ChantryDetailView,
        "caern": CaernDetailView,
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


class ItemCreateView(CreateView):
    model = Item
    fields = "__all__"
    template_name = "wod/items/item/create.html"


class WonderDetailView(DetailView):
    model = Wonder
    template_name = "wod/items/wonder/detail.html"


class WonderCreateView(CreateView):
    model = Wonder
    fields = "__all__"
    template_name = "wod/items/wonder/create.html"


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
        context = {
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
        all_rotes = list(context["object"].rotes.all())
        row_length = 2
        all_rotes = [
            all_rotes[i : i + row_length] for i in range(0, len(all_rotes), row_length)
        ]
        if len(all_rotes) != 0:
            while len(all_rotes[-1]) < row_length:
                all_rotes[-1].append(empty_rote)
        context["rotes"] = all_rotes
        context["year"] = abs(grimoire.date_written)
        return context


class GrimoireCreateView(CreateView):
    model = Grimoire
    fields = "__all__"
    template_name = "wod/items/grimoire/create.html"


class LibraryDetailView(DetailView):
    model = Library
    template_name = "wod/items/library/detail.html"


class LibraryCreateView(CreateView):
    model = Library
    fields = "__all__"
    template_name = "wod/items/libtary/create.html"


class FetishDetailView(DetailView):
    model = Fetish
    template_name = "wod/items/fetish/detail.html"


class GenericItemDetailView(View):
    views = {
        "item": ItemDetailView,
        "wonder": WonderDetailView,
        "grimoire": GrimoireDetailView,
        "library": LibraryDetailView,
        "fetish": FetishDetailView,
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


class CharacterCreateView(CreateView):
    model = Character
    fields = "__all__"
    template_name = "wod/characters/character/create.html"


class HumanDetailView(DetailView):
    model = Human
    template_name = "wod/characters/human/detail.html"


class HumanCreateView(CreateView):
    model = Human
    fields = "__all__"
    template_name = "wod/characters/human/create.html"


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


class WerewolfCreateView(CreateView):
    model = Werewolf
    fields = "__all__"
    template_name = "wod/characters/werewolf/create.html"


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

        secondary_talents = [
            [f"{k.replace('_', ' ').title()}", v, context[f"{k}_spec"]]
            for k, v in mage.get_talents().items()
            if k not in PRIMARY_ABILITIES and v != 0
        ]
        secondary_skills = [
            [f"{k.replace('_', ' ').title()}", v, context[f"{k}_spec"]]
            for k, v in mage.get_skills().items()
            if k not in PRIMARY_ABILITIES and v != 0
        ]
        secondary_knowledges = [
            [f"{k.replace('_', ' ').title()}", v, context[f"{k}_spec"]]
            for k, v in mage.get_knowledges().items()
            if k not in PRIMARY_ABILITIES and v != 0
        ]

        for triple in secondary_knowledges:
            if triple[0] == "History Knowledge":
                triple[0] = "History"

        secondary_talents.sort(key=lambda x: x[0])
        secondary_skills.sort(key=lambda x: x[0])
        secondary_knowledges.sort(key=lambda x: x[0])
        num_sec_tal = len(secondary_talents)
        num_sec_ski = len(secondary_skills)
        num_sec_kno = len(secondary_knowledges)
        m = max(num_sec_tal, num_sec_ski, num_sec_kno)
        for _ in range(m - num_sec_tal):
            secondary_talents.append(("", 0, []))
        for _ in range(m - num_sec_ski):
            secondary_skills.append(("", 0, []))
        for _ in range(m - num_sec_kno):
            secondary_knowledges.append(("", 0, []))
        context["secondaries"] = list(
            zip(secondary_talents, secondary_skills, secondary_knowledges)
        )
        return context


class MageCreateView(CreateView):
    model = Mage
    form_class = MageForm
    # fields = "__all__"
    template_name = "wod/characters/mage/create.html"


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
        "cabal": Cabal,
        "pack": Pack,
    }

    def post(self, request, *args, **kwargs):
        if request.POST["character_type"] in ["werewolf", "mage"]:
            char = self.chars[request.POST["character_type"]].objects.create(
                name=request.POST["character_name"], player=request.user
            )
        else:
            char = self.chars[request.POST["character_type"]].objects.create(
                name=request.POST["character_name"]
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


class GroupDetailView(DetailView):
    model = Group
    template_name = "wod/characters/group/detail.html"


class GroupCreateView(CreateView):
    model = Group
    fields = "__all__"
    template_name = "wod/characters/group/create.html"


class CabalDetailView(DetailView):
    model = Cabal
    template_name = "wod/characters/cabal/detail.html"


class CabalCreateView(CreateView):
    model = Cabal
    fields = "__all__"
    template_name = "wod/characters/cabal/create.html"


class PackDetailView(DetailView):
    model = Pack
    template_name = "wod/characters/pack/detail.html"


class PackCreateView(CreateView):
    model = Pack
    fields = "__all__"
    template_name = "wod/characters/pack/create.html"


class GenericGroupDetailView(View):
    group_views = {
        "group": GroupDetailView,
        "cabal": CabalDetailView,
        "pack": PackDetailView,
    }

    def get(self, request, *args, **kwargs):
        group = Group.objects.get(pk=kwargs["pk"])
        if group.type in self.group_views:
            return self.group_views[group.type].as_view()(request, *args, **kwargs)
        return redirect("wod:characters_index")


class NodeMeritFlawDetailView(DetailView):
    model = NodeMeritFlaw
    template_name = "wod/locations/nodemeritflaw/detail.html"


class ArchetypeDetailView(DetailView):
    model = Archetype
    template_name = "wod/characters/archetype/detail.html"


class CampDetailView(DetailView):
    model = Camp
    template_name = "wod/characters/camp/detail.html"


class GiftDetailView(DetailView):
    model = Gift
    template_name = "wod/characters/gift/detail.html"


class InstrumentDetailView(DetailView):
    model = Instrument
    template_name = "wod/characters/instrument/detail.html"


class MageFactionDetailView(DetailView):
    model = MageFaction
    template_name = "wod/characters/magefaction/detail.html"


class MeritFlawDetailView(DetailView):
    model = MeritFlaw
    template_name = "wod/characters/meritflaw/detail.html"


class ParadigmDetailView(DetailView):
    model = Paradigm
    template_name = "wod/characters/paradigm/detail.html"


class PracticeDetailView(DetailView):
    model = Practice
    template_name = "wod/characters/practice/detail.html"


class RenownIncidentDetailView(DetailView):
    model = RenownIncident
    template_name = "wod/characters/renownincident/detail.html"


class ResonanceDetailView(DetailView):
    model = Resonance
    template_name = "wod/characters/resonance/detail.html"


class RiteDetailView(DetailView):
    model = Rite
    template_name = "wod/characters/rite/detail.html"


class RoteDetailView(DetailView):
    model = Rote
    template_name = "wod/characters/rote/detail.html"


class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = "wod/characters/specialty/detail.html"


class TotemDetailView(DetailView):
    model = Totem
    template_name = "wod/characters/totem/detail.html"


class TribeDetailView(DetailView):
    model = Tribe
    template_name = "wod/characters/tribe/detail.html"
