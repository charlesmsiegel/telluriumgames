from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View
from django.views.generic.list import ListView

from tc.models import *
from tc.forms import AberrantForm


# Create your views here.
class IndexView(View):
    """Class that manages the Index view"""

    def get(self, request):
        context = self.get_context()
        return render(request, "tc/characters/index.html", context)

    def post(self, request):
        context = self.get_context()
        return render(request, "tc/characters/index.html", context)

    def get_context(self):
        chars = Aberrant.objects.all().order_by("name")
        context = {}
        context["chars"] = chars
        return context


class AberrantCreateView(CreateView):
    model = Aberrant
    form_class = AberrantForm
    template_name = "tc/characters/aberrant/create.html"


class AberrantDetailView(View):
    def get(self, request, pk):
        context = self.get_context(pk)
        return render(request, "tc/characters/aberrant/detail.html", context)

    def get_context(self, pk):
        char = Aberrant.objects.get(id=pk)
        context = {"character": char}
        attribute_ratings = AttributeRating.objects.filter(character=char)
        for attribute in attribute_ratings:
            context[attribute.attribute.name.lower()] = attribute
        megaattribute_ratings = MegaAttributeRating.objects.filter(character=char)
        for attribute in megaattribute_ratings:
            context[
                attribute.megaattribute.name.lower().replace("-", "_").replace(" ", "_")
            ] = attribute
        skill_ratings = SkillRating.objects.filter(character=char)
        for skill in skill_ratings:
            context[
                skill.skill.name.lower().replace("-", "_").replace(" ", "_")
            ] = skill

        origin_path = PathConnectionRating.objects.filter(
            character=char, path__type="ORI"
        ).first()
        role_path = PathConnectionRating.objects.filter(
            character=char, path__type="ROL"
        ).first()
        society_path = PathConnectionRating.objects.filter(
            character=char, path__type="SOC"
        ).first()
        context["origin_path"] = origin_path
        context["role_path"] = role_path
        context["society_path"] = society_path
        additional_paths = list(PathConnectionRating.objects.filter(character=char))
        additional_paths.remove(origin_path)
        additional_paths.remove(role_path)
        additional_paths.remove(society_path)
        context["additional_paths"] = additional_paths

        edges = EdgeRating.objects.filter(character=char).order_by("edge")
        edges = [
            x
            for x in edges
            if x.edge.name not in [x.name for x in MegaEdge.objects.all()]
        ]
        context["edges"] = edges

        context["enhancededges"] = list(char.enhanced_edges.all())

        megaedges = MegaEdgeRating.objects.filter(character=char).order_by("megaedge")
        context["megaedges"] = megaedges
        powers = PowerRating.objects.filter(character=char)
        context["powers"] = powers.order_by("power")
        tags = TagRating.objects.filter(power__in=powers).order_by("tag")
        context["tags"] = tags
        context["transformations"] = char.transformations.all()
        tricks = []
        for skill in skill_ratings:
            tricks.extend(skill.tricks.all())
        context["tricks"] = tricks
        context["tricks"].sort(key=lambda x: x.name)

        health_levels = []
        for _ in range(char.bruised_levels):
            health_levels.append("+1")
        for _ in range(char.injured_levels):
            health_levels.append("+2")
        for _ in range(char.maimed_levels):
            health_levels.append("+4")
        context["health_levels"] = health_levels
        return context


class TrickDetailView(DetailView):
    model = Trick
    template_name = "tc/characters/trick.html"


class EdgeDetailView(DetailView):
    model = Edge
    template_name = "tc/characters/edge.html"


class EnhancedEdgeDetailView(DetailView):
    model = EnhancedEdge
    template_name = "tc/characters/enhancededge.html"


class MegaEdgeDetailView(DetailView):
    model = MegaEdge
    template_name = "tc/characters/aberrant/megaedge.html"


class PathDetailView(DetailView):
    model = Path
    template_name = "tc/characters/path.html"


class TagDetailView(DetailView):
    model = Tag
    template_name = "tc/characters/aberrant/tag.html"


class TransformationDetailView(DetailView):
    model = Transformation
    template_name = "tc/characters/aberrant/transformation.html"


class PowerDetailView(DetailView):
    model = Power
    template_name = "tc/characters/aberrant/power.html"


class AberrantUpdate(UpdateView):
    model = Aberrant
    fields = "__all__"
    template_name = "tc/characters/aberrant/update.html"


class RandomCreateView(View):
    def post(self, request):
        char = Aberrant.objects.create(player=request.user)
        char.random(name=request.POST["character_name"], xp=int(request.POST["xp"]))
        char.save()
        return redirect(f"tc/characters/{char.id}")

    def get(self, request):
        return redirect("tc/characters/")


from django.db.models import Q


class EdgeListView(ListView):
    model = Edge

    def get_queryset(self, *args, **kwargs):
        qs = super(EdgeListView, self).get_queryset(*args, **kwargs)
        # edges = EdgeRating.objects.filter(character=char).order_by("edge")
        qs = [
            x.name for x in qs if x.name not in [x.name for x in MegaEdge.objects.all()]
        ]
        qs = Edge.objects.filter(name__in=qs)
        # qs = qs.filter(~Q(name__in=MegaEdge.objects.all()))
        return qs


class EnhancedEdgeListView(ListView):
    model = EnhancedEdge


class MegaEdgeListView(ListView):
    model = MegaEdge


class PathListView(ListView):
    model = Path


class PowerListView(ListView):
    model = Power


class TagListView(ListView):
    model = Tag


class TransformationListView(ListView):
    model = Transformation


class TrickListView(ListView):
    model = Trick
