from django.views.generic import CreateView, DetailView, UpdateView

from wod.models.locations.werewolf import Caern


class CaernDetailView(DetailView):
    model = Caern
    template_name = "wod/locations/werewolf/caern/detail.html"


class CaernCreateView(CreateView):
    model = Caern
    fields = "__all__"
    template_name = "wod/locations/werewolf/caern/create.html"


class CaernUpdateView(UpdateView):
    model = Caern
    fields = "__all__"
    template_name = "wod/locations/werewolf/caern/update.html"
