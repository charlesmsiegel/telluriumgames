from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, View

from exalted.models.characters.mortals import MeritRating, Mortal, Specialty, Intimacy, Merit


# Create your views here.
class IndexView(View):
    """Class that manages the Index view"""

    def get(self, request):
        context = self.get_context()
        return render(request, "exalted/characters/index.html", context)

    def post(self, request):
        context = self.get_context()
        return render(request, "exalted/characters/index.html", context)

    def get_context(self):
        chars = Mortal.objects.all().order_by("name")
        context = {}
        context["chars"] = chars
        return context


class MortalDetailView(View):
    def get(self, request, *args, **kwargs):
        char = Mortal.objects.get(pk=kwargs["pk"])
        context = {
            "object": char,
            "merits": MeritRating.objects.filter(character=char).order_by(
                "merit__name"
            ),
            "specialties": char.specialties.all().order_by("name"),
        }
        return render(request, "exalted/characters/mortal/detail.html", context,)


class MortalCreateView(CreateView):
    model = Mortal
    fields = "__all__"
    template_name = "exalted/characters/mortal/create.html"


class CharacterDetailView(View):
    """Class that manages Views for characters"""

    create_views = {
        "mortal": MortalDetailView,
    }

    def get(self, request, *args, **kwargs):
        char = Mortal.objects.get(pk=kwargs["pk"])
        if char.type in self.create_views:
            return self.create_views[char.type].as_view()(request, *args, **kwargs)
        return redirect("exalted:characters_index")


class RandomCharacterView(View):
    chars = {
        "mortal": Mortal,
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
        return redirect("exalted:characters_index")

class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = "exalted/characters/specialty/detail.html"
    
class IntimacyDetailView(DetailView):
    model = Intimacy
    template_name = "exalted/characters/intimacy/detail.html"
    
class MeritDetailView(DetailView):
    model = Merit
    template_name = "exalted/characters/merit/detail.html"