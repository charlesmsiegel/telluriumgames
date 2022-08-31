from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, View

from wod.models.locations.mage import (
    Chantry,
    Node,
    NodeMeritFlaw,
    NodeMeritFlawRating,
    NodeResonanceRating,
    Sector,
)


class SectorDetailView(DetailView):
    model = Sector
    template_name = "wod/locations/mage/sector/detail.html"


class SectorCreateView(CreateView):
    model = Sector
    fields = "__all__"
    template_name = "wod/locations/mage/sector/form.html"


class SectorUpdateView(UpdateView):
    model = Sector
    fields = "__all__"
    template_name = "wod/locations/mage/sector/form.html"


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
    template_name = "wod/locations/mage/node/form.html"


class NodeUpdateView(UpdateView):
    model = Node
    fields = "__all__"
    template_name = "wod/locations/mage/node/form.html"


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
    template_name = "wod/locations/mage/chantry/form.html"


class ChantryUpdateView(UpdateView):
    model = Chantry
    fields = "__all__"
    template_name = "wod/locations/mage/chantry/form.html"


class NodeMeritFlawDetailView(DetailView):
    model = NodeMeritFlaw
    template_name = "wod/locations/mage/nodemeritflaw/detail.html"


class NodeMeritFlawCreateView(CreateView):
    model = NodeMeritFlaw
    fields = "__all__"
    template_name = "wod/locations/mage/nodemeritflaw/form.html"


class NodeMeritFlawUpdateView(UpdateView):
    model = NodeMeritFlaw
    fields = "__all__"
    template_name = "wod/locations/mage/nodemeritflaw/form.html"
