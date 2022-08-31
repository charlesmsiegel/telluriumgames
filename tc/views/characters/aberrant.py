from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from tc.models.characters.aberrant import (
    Aberrant,
    MegaEdge,
    MegaEdgeRating,
    Power,
    PowerRating,
    Tag,
    Transformation,
)
from tc.views.characters.human import HumanDetailView


class AberrantDetailView(HumanDetailView):
    def get(self, request, pk):
        context = self.get_context(pk)
        return render(request, "tc/characters/aberrant/aberrant/detail.html", context)

    def get_context(self, pk):
        context = super().get_context(pk=pk)
        context["mega_edges"] = MegaEdgeRating.objects.filter(
            character=context["character"]
        )
        context["powers"] = PowerRating.objects.filter(character=context["character"])
        return context


class AberrantCreateView(CreateView):
    model = Aberrant
    fields = "__all__"
    template_name = "tc/characters/aberrant/aberrant/form.html"


class AberrantUpdateView(UpdateView):
    model = Aberrant
    fields = "__all__"
    template_name = "tc/characters/aberrant/aberrant/form.html"


class MegaEdgeDetailView(DetailView):
    model = MegaEdge
    template_name = "tc/characters/aberrant/megaedge/detail.html"


class MegaEdgeCreateView(CreateView):
    model = MegaEdge
    fields = "__all__"
    template_name = "tc/characters/aberrant/megaedge/form.html"


class MegaEdgeUpdateView(UpdateView):
    model = MegaEdge
    fields = "__all__"
    template_name = "tc/characters/aberrant/megaedge/form.html"


class PowerDetailView(DetailView):
    model = Power
    template_name = "tc/characters/aberrant/power/detail.html"


class PowerCreateView(CreateView):
    model = Power
    fields = "__all__"
    template_name = "tc/characters/aberrant/power/form.html"


class PowerUpdateView(UpdateView):
    model = Power
    fields = "__all__"
    template_name = "tc/characters/aberrant/power/form.html"


class TagDetailView(DetailView):
    model = Tag
    template_name = "tc/characters/aberrant/tag/detail.html"


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    template_name = "tc/characters/aberrant/tag/form.html"


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "tc/characters/aberrant/tag/form.html"


class TransformationDetailView(DetailView):
    model = Transformation
    template_name = "tc/characters/aberrant/transformation/detail.html"


class TransformationCreateView(CreateView):
    model = Transformation
    fields = "__all__"
    template_name = "tc/characters/aberrant/transformation/form.html"


class TransformationUpdateView(UpdateView):
    model = Transformation
    fields = "__all__"
    template_name = "tc/characters/aberrant/transformation/form.html"
