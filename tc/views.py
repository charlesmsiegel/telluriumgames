from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, View

from tc.models.characters.aberrant import (
    Aberrant,
    MegaEdge,
    MegaEdgeRating,
    Power,
    PowerRating,
    Tag,
    Transformation,
)
from tc.models.characters.human import (
    Edge,
    EdgeRating,
    EnhancedEdge,
    Human,
    Path,
    PathConnection,
    PathRating,
    Specialty,
    Trick,
)
from tc.models.characters.talent import Gift, MomentOfInspiration, Talent


# Create your views here.
class IndexView(View):
    """Class that manages the Index view"""

    def get(self, request):
        context = self.get_context()
        return render(request, "tc/characters/index.html", context)

    def get_context(self):
        chars = Human.objects.all().order_by("name")
        context = {}
        context["chars"] = chars
        return context


class HumanDetailView(View):
    def get(self, request, pk):
        context = self.get_context(pk)
        return render(request, "tc/characters/human/detail.html", context)

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
    template_name = "tc/characters/human/create.html"


class TalentDetailView(HumanDetailView):
    def get(self, request, pk):
        context = self.get_context(pk)
        return render(request, "tc/characters/talent/detail.html", context)

    def get_context(self, pk):
        context = super().get_context(pk=pk)
        return context


class TalentCreateView(CreateView):
    model = Talent
    fields = "__all__"
    template_name = "tc/characters/talent/create.html"


class AberrantDetailView(HumanDetailView):
    def get(self, request, pk):
        context = self.get_context(pk)
        return render(request, "tc/characters/aberrant/detail.html", context)

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
    template_name = "tc/characters/aberrant/create.html"


class CharacterDetailView(View):
    detail_views = {
        "human": HumanDetailView,
        "talent": TalentDetailView,
        "aberrant": AberrantDetailView,
    }

    def get(self, request, *args, **kwargs):
        char = Human.objects.get(pk=kwargs["pk"])
        if char.type in self.detail_views:
            return self.detail_views[char.type].as_view()(request, *args, **kwargs)
        return redirect("tc:characters:index")


class RandomCharacterView(View):
    chars = {
        "human": Human,
        "talent": Talent,
        "aberrant": Aberrant,
    }

    def post(self, request, *args, **kwargs):
        char = self.chars[request.POST["char_type"]].objects.create(
            name=request.POST["char_name"], player=request.user
        )
        try:
            xp = int(request.POST["xp"])
        except ValueError:
            xp = 0
        xp = max(xp, 0)
        char.random(xp=xp)
        char.save()
        return redirect(char.get_absolute_url())

    def get(self, request):
        return redirect("cod:characters:index")


class EdgeDetailView(DetailView):
    model = Edge
    template_name = "tc/characters/edge/detail.html"


class EnhancedEdgeDetailView(DetailView):
    model = EnhancedEdge
    template_name = "tc/characters/enhancededge/detail.html"


class GiftDetailView(DetailView):
    model = Gift
    template_name = "tc/characters/gift/detail.html"


class MegaEdgeDetailView(DetailView):
    model = MegaEdge
    template_name = "tc/characters/megaedge/detail.html"


class MomentOfInspirationDetailView(DetailView):
    model = MomentOfInspiration
    template_name = "tc/characters/momentofinspiration/detail.html"


class PathDetailView(DetailView):
    model = Path
    template_name = "tc/characters/path/detail.html"


class PathConnectionDetailView(DetailView):
    model = PathConnection
    template_name = "tc/characters/pathconnection/detail.html"


class PowerDetailView(DetailView):
    model = Power
    template_name = "tc/characters/power/detail.html"


class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = "tc/characters/specialty/detail.html"


class TagDetailView(DetailView):
    model = Tag
    template_name = "tc/characters/tag/detail.html"


class TransformationDetailView(DetailView):
    model = Transformation
    template_name = "tc/characters/transformation/detail.html"


class TrickDetailView(DetailView):
    model = Trick
    template_name = "tc/characters/trick/detail.html"
