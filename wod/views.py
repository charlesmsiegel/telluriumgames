from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View
from wod.forms import LocationForm, MageForm
from wod.models.characters import Character, Mage, MageFaction
from wod.models.locations.mage import City, Location, Node
from wod.models.objects.mage import Grimoire, Wonder


# Create your views here.
class IndexView(View):
    """Class that manages the Index view"""

    def get(self, request):
        context = self.get_context()
        return render(request, "wod/characters/index.html", context)

    def post(self, request):
        context = self.get_context()
        # character_class_dict = {
        #     # "vampire": Vampire,
        #     # "werewolf": Werewolf,
        #     "mage": Mage,
        #     # "wraith": Wraith,
        #     # "changeling": Changeling,
        # }
        # if request.POST["character_type"] in character_class_dict:
        #     char_cl = character_class_dict[request.POST["character_type"]]
        #     character = char_cl.objects.create(
        #         name=request.POST["character_name"], player=request.user
        #     )
        #     return redirect(character.get_absolute_url())
        return render(request, "wod/characters/index.html", context)

    def get_context(self):
        chars = Character.objects.all().order_by("name")
        context = {}
        context["chars"] = chars
        return context


class MageCreateView(CreateView):
    """Class that manages the Mage Create view"""

    model = Mage
    form_class = MageForm
    template_name = "wod/characters/mage/create.html"


class MageDetailView(DetailView):
    """Class that manages Views for mages"""

    model = Mage
    template_name = "wod/characters/mage/detail.html"


class MageUpdate(UpdateView):
    """Class that manages the Mage Update view"""

    model = Mage
    fields = "__all__"
    template_name = "wod/characters/mage/update.html"


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


class CharacterDetailView(View):
    """Class that manages Views for characters"""

    create_views = {
        # "vampire": VampireView,
        # "werewolf": WerewolfView,
        "mage": MageDetailView,
        # "changeling": ChangelingView,
        # "wraith": WraithView,
    }

    def get(self, request, *args, **kwargs):
        char = Character.objects.get(pk=kwargs["pk"])
        if char.type in self.create_views:
            return self.create_views[char.type].as_view()(request, *args, **kwargs)
        return redirect("wod:characters_index")


def recurse_records(nested_dict, count=0, nested_list=None):
    if nested_list is None:
        nested_list = []
    for key in nested_dict.keys():
        nested_list.append((range(count), key))
        nested_list = recurse_records(
            nested_dict[key], count=count + 1, nested_list=nested_list
        )
    return nested_list


def location_index(request):
    locations = Location.objects.all()
    loc_form = LocationForm()
    context = {}
    context["locations"] = locations
    context["location_form"] = loc_form

    hierarchy = {}
    for loc in locations:
        hierarchy[loc] = {}

    for_removal = []
    for key, value in hierarchy.items():
        if key.parent in hierarchy:
            hierarchy[key.parent].update({key: value})
            for_removal.append(key)
    for key in for_removal:
        hierarchy.pop(key)

    context["location_pairs"] = recurse_records(hierarchy)
    seen = set()
    seen_add = seen.add
    context["location_pairs"] = [
        x for x in context["location_pairs"] if not (x in seen or seen_add(x))
    ]

    if request.method == "POST":
        location_form = LocationForm(request.POST)
        parent = None
        if request.POST["parent"]:
            parent = get_object_or_404(Location, pk=location_form.data["parent"])
        new_loc = Location.objects.create(
            name=location_form.data["name"],
            parent=parent,
            description=location_form.data["description"],
        )
        return redirect(new_loc.get_absolute_url())
    return render(request, "wod/locations/index.html", context)


class LocationDetailView(DetailView):
    """Class that manages Views for Location"""

    model = Location
    template_name = "wod/locations/location.html"


class CityDetailView(DetailView):
    """Class that manages Views for City"""

    model = City
    template_name = "wod/locations/city.html"


class NodeDetailView(DetailView):
    """Class that manages Views for Node"""

    model = Node
    template_name = "wod/locations/mage/node.html"


class GenericLocationDetailView(View):
    """Class that manages Views for locations"""

    create_views = {
        "location": LocationDetailView,
        "city": CityDetailView,
        "node": NodeDetailView,
    }

    def get(self, request, *args, **kwargs):
        location = Location.objects.get(pk=kwargs["pk"])
        if location.type in self.create_views:
            return self.create_views[location.type].as_view()(request, *args, **kwargs)
        return redirect("wod:location_index")


class WonderDetailView(DetailView):
    """Class that manages Views for wonders"""

    model = Wonder
    template_name = "wod/objects/mage/wonder.html"


class GrimoireDetailView(View):
    """Class that manages Views for grimoires"""

    def get(self, request, *args, **kwargs):
        context = self.get_context(*args, **kwargs)
        return render(request, "wod/objects/mage/grimoire.html", context)

    def get_context(self, *args, **kwargs):
        g = Grimoire.objects.get(pk=kwargs["pk"])
        faction_list = [g.faction]
        while faction_list[-1].parent is not None:
            faction_list.append(faction_list[-1].parent)
        faction_list = faction_list[::-1]
        faction_list = [str(x) for x in faction_list]
        faction = "/".join(faction_list)
        spheres = ", ".join([x.replace("_", " ").title() for x in g.spheres])
        abilities = ", ".join([x.replace("_", " ").title() for x in g.abilities])
        paradigms = ", ".join([str(x) for x in g.paradigms.all()])
        practices = ", ".join([str(x) for x in g.practices.all()])
        instruments = ", ".join([str(x) for x in g.instruments.all()])
        d = {
            "object": g,
            "spheres": spheres,
            "abilities": abilities,
            "faction": faction,
            "paradigms": paradigms,
            "practices": practices,
            "instruments": instruments,
        }
        return d


class GenericWonderDetailView(View):
    """Class that manages Views for wonders"""

    create_views = {"wonder": WonderDetailView, "grimoire": GrimoireDetailView}

    def get(self, request, *args, **kwargs):
        wonder = Wonder.objects.get(pk=kwargs["pk"])
        if wonder.type in self.create_views:
            return self.create_views[wonder.type].as_view()(request, *args, **kwargs)
        return redirect("wonders_index")


class ObjectIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, "wod/objects/index.html", {"objects": Wonder.objects.all()}
        )

