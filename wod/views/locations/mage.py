from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, View

from wod.models.locations.mage import (
    Node,
    NodeMeritFlawRating,
    NodeResonanceRating,
    Sector,
    Chantry,
    NodeMeritFlaw,
)


class SectorDetailView(DetailView):
    model = Sector
    template_name = "wod/locations/mage/sector/detail.html"


class SectorCreateView(CreateView):
    model = Sector
    fields = "__all__"
    template_name = "wod/locations/mage/sector/create.html"


class SectorUpdateView(UpdateView):
    model = Sector
    fields = "__all__"
    template_name = "wod/locations/mage/sector/update.html"


class NodeDetailView(View):
    def get(self, request, *args, **kwargs):
        node = Node.objects.get(pk=kwargs["pk"])
        context = self.get_context(node)
        return render(request, "wod/locations/mage/node/detail.html", context)

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
    template_name = "wod/locations/mage/node/create.html"


class SectorUpdateView(UpdateView):
    model = Node
    fields = "__all__"
    template_name = "wod/locations/mage/node/update.html"


class ChantryDetailView(View):
    def get(self, request, *args, **kwargs):
        chantry = Chantry.objects.get(pk=kwargs["pk"])
        context = self.get_context(chantry)
        return render(request, "wod/locations/mage/chantry/detail.html", context)

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
    template_name = "wod/locations/mage/chantry/create.html"


class SectorUpdateView(UpdateView):
    model = Chantry
    fields = "__all__"
    template_name = "wod/locations/mage/chantry/update.html"


class NodeMeritFlawDetailView(DetailView):
    model = NodeMeritFlaw
    template_name = "wod/locations/mage/nodemeritflaw/detail.html"


class NodeMeritFlawCreateView(CreateView):
    model = NodeMeritFlaw
    fields = "__all__"
    template_name = "wod/locations/mage/nodemeritflaw/create.html"


class NodeMeritFlawUpdateView(UpdateView):
    model = NodeMeritFlaw
    fields = "__all__"
    template_name = "wod/locations/mage/nodemeritflaw/update.html"
