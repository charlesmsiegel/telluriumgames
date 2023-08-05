from django.views.generic import CreateView, DetailView, UpdateView

from exalted.models.locations.mortals import ExLocation


class ExLocationDetailView(DetailView):
    model = ExLocation
    template_name = "exalted/locations/mortals/exlocation/detail.html"


class ExLocationCreateView(CreateView):
    model = ExLocation
    fields = [
        "name",
        "parent",
        "gauntlet",
        "shroud",
        "dimension_barrier",
        "reality_zone",
        "description",
    ]
    template_name = "exalted/locations/mortals/exlocation/form.html"


class ExLocationUpdateView(UpdateView):
    model = ExLocation
    fields = [
        "name",
        "parent",
        "gauntlet",
        "shroud",
        "dimension_barrier",
        "reality_zone",
        "description",
    ]
    template_name = "exalted/locations/mortals/exlocation/form.html"
