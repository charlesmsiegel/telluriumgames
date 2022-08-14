from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from tc.models.characters.human import (
    Edge,
    EdgeRating,
    EnhancedEdge,
    Human,
    TCPath,
    PathConnection,
    PathRating,
    Specialty,
    Trick,
)


class HumanDetailView(View):
    def get(self, request, pk):
        context = self.get_context(pk)
        return render(request, "tc/characters/human/human/detail.html", context)

    def get_context(self, pk):
        char = Human.objects.get(id=pk)
        context = {"character": char}
        context["origin_path"] = PathRating.objects.filter(
            character=char, path__type="origin"
        ).first()
        context["role_path"] = PathRating.objects.filter(
            character=char, path__type="role"
        ).first()
        context["society_path"] = PathRating.objects.filter(
            character=char, path__type="society"
        ).first()
        context["additional_paths"] = [
            x
            for x in PathRating.objects.filter(character=char)
            if x
            not in [
                context["origin_path"],
                context["role_path"],
                context["society_path"],
            ]
        ]
        for skill in char.get_skills():
            context[skill + "_spec"] = ", ".join(
                [x.name for x in char.specialties.filter(skill=skill)]
            )
        context["edges"] = EdgeRating.objects.filter(character=char)
        return context


class HumanCreateView(CreateView):
    model = Human
    fields = "__all__"
    template_name = "tc/characters/human/human/create.html"


class HumanUpdateView(UpdateView):
    model = Human
    fields = "__all__"
    template_name = "tc/characters/human/human/update.html"


class EdgeDetailView(DetailView):
    model = Edge
    template_name = "tc/characters/human/edge/detail.html"


class EdgeCreateView(CreateView):
    model = Edge
    fields = "__all__"
    template_name = "tc/characters/human/edge/create.html"


class EdgeUpdateView(UpdateView):
    model = Edge
    fields = "__all__"
    template_name = "tc/characters/human/edge/update.html"


class EnhancedEdgeDetailView(DetailView):
    model = EnhancedEdge
    template_name = "tc/characters/human/enhancededge/detail.html"


class EnhancedEdgeCreateView(CreateView):
    model = EnhancedEdge
    fields = "__all__"
    template_name = "tc/characters/human/enhancededge/create.html"


class EnhancedEdgeUpdateView(UpdateView):
    model = EnhancedEdge
    fields = "__all__"
    template_name = "tc/characters/human/enhancededge/update.html"


class PathDetailView(DetailView):
    model = TCPath
    template_name = "tc/characters/human/path/detail.html"


class PathCreateView(CreateView):
    model = TCPath
    fields = "__all__"
    template_name = "tc/characters/human/path/create.html"


class PathUpdateView(UpdateView):
    model = TCPath
    fields = "__all__"
    template_name = "tc/characters/human/path/update.html"


class PathConnectionDetailView(DetailView):
    model = PathConnection
    template_name = "tc/characters/human/pathconnection/detail.html"


class PathConnectionCreateView(CreateView):
    model = PathConnection
    fields = "__all__"
    template_name = "tc/characters/human/pathconnection/create.html"


class PathConnectionUpdateView(UpdateView):
    model = PathConnection
    fields = "__all__"
    template_name = "tc/characters/human/pathconnection/update.html"


class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = "tc/characters/human/specialty/detail.html"


class SpecialtyCreateView(CreateView):
    model = Specialty
    fields = "__all__"
    template_name = "tc/characters/human/specialty/create.html"


class SpecialtyUpdateView(UpdateView):
    model = Specialty
    fields = "__all__"
    template_name = "tc/characters/human/specialty/update.html"


class TrickDetailView(DetailView):
    model = Trick
    template_name = "tc/characters/human/trick/detail.html"


class TrickCreateView(CreateView):
    model = Trick
    fields = "__all__"
    template_name = "tc/characters/human/trick/create.html"


class TrickUpdateView(UpdateView):
    model = Trick
    fields = "__all__"
    template_name = "tc/characters/human/trick/update.html"
