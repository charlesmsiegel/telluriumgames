from django.views.generic import CreateView, DetailView, UpdateView

from wod.models.locations.human import City, Location


class LocationDetailView(DetailView):
    model = Location
    template_name = "wod/locations/human/location/detail.html"


class LocationCreateView(CreateView):
    model = Location
    fields = "__all__"
    template_name = "wod/locations/human/location/form.html"


class LocationUpdateView(UpdateView):
    model = Location
    fields = "__all__"
    template_name = "wod/locations/human/location/form.html"


class CityDetailView(DetailView):
    model = City
    template_name = "wod/locations/human/city/detail.html"


class CityCreateView(CreateView):
    model = City
    fields = "__all__"
    template_name = "wod/locations/human/city/form.html"


class CityUpdateView(UpdateView):
    model = City
    fields = "__all__"
    template_name = "wod/locations/human/city/form.html"
