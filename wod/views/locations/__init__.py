from django.shortcuts import redirect, render
from django.views.generic import View

from core.utils import level_name, tree_sort
from wod.forms import RandomLocationForm
from wod.models.locations.human import Location
from wod.models.locations.mage import Chantry, Node

from . import human, mage, werewolf


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
        context["form"] = RandomLocationForm
        L1 = []
        L2 = []
        for x in Location.objects.filter(parent=None).order_by("name"):
            L1.extend([level_name(y) for y in tree_sort(x)])
            L2.extend(tree_sort(x))

        context["names_dict"] = dict(zip(L1, L2))
        return context


def load_location_types(request):
    locations = {
        # "werewolf": [],
        "mage": ["node", "chantry", "library"],
    }
    gameline = request.GET.get("gameline")
    location_types = locations[gameline]
    return render(
        request,
        "wod/locations/load_location_dropdown_list.html",
        {"location_types": location_types},
    )


class GenericLocationDetailView(View):
    views = {
        "location": human.LocationDetailView,
        "city": human.CityDetailView,
        "node": mage.NodeDetailView,
        "chantry": mage.ChantryDetailView,
        "caern": werewolf.CaernDetailView,
        "sector": mage.SectorDetailView,
        "library": mage.LibraryDetailView,
    }

    def get(self, request, *args, **kwargs):
        loc = Location.objects.get(pk=kwargs["pk"])
        if loc.type in self.views:
            return self.views[loc.type].as_view()(request, *args, **kwargs)
        return redirect("wod:locations:index")


class RandomLocationView(View):
    locs = {
        "node": Node,
        "chantry": Chantry,
    }

    def post(self, request):
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        location = self.locs[request.POST["location_type"]].objects.create(
            name=request.POST["name"], owner=user
        )
        if request.POST["rank"] is None:
            rank = None
        else:
            rank = int(request.POST["rank"])
        location.random(rank=rank)
        location.save()
        return redirect(location.get_absolute_url())

    def get(self, request):
        return redirect("wod:locations:index")
