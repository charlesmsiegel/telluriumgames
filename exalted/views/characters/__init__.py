from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, View

from exalted.forms import RandomCharacterForm
from exalted.models.characters.dragonblooded import DragonBlooded
from exalted.models.characters.mortals import ExMortal
from exalted.models.characters.solars import Solar

from . import dragonblooded, mortal, solars


class IndexView(View):
    """Class that manages the Index view"""

    def get(self, request):
        context = self.get_context()
        return render(request, "exalted/characters/index.html", context)

    def post(self, request):
        context = self.get_context()
        return render(request, "exalted/characters/index.html", context)

    def get_context(self):
        chars = ExMortal.objects.filter(chronicle=None).order_by("name")
        context = {}
        context["chars"] = chars
        context["form"] = RandomCharacterForm
        return context


class GenericCharacterDetailView(View):
    """Class that manages Views for characters"""

    create_views = {
        "mortal": mortal.MortalDetailView,
        "solar": solars.SolarDetailView,
        "dragon-blooded": dragonblooded.DragonBloodedDetailView,
    }

    def get(self, request, *args, **kwargs):
        char = ExMortal.objects.get(pk=kwargs["pk"])
        if char.type in self.create_views:
            return self.create_views[char.type].as_view()(request, *args, **kwargs)
        return redirect("exalted:characters:index")

    def post(self, request, *args, **kwargs):
        char = ExMortal.objects.get(pk=kwargs["pk"])
        if char.type in self.create_views:
            return self.create_views[char.type].as_view()(request, *args, **kwargs)
        return redirect("exalted:characters:index")


class RandomCharacterView(View):
    chars = {"mortal": ExMortal, "solar": Solar, "dragonblooded": DragonBlooded}

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        char = self.chars[request.POST["character_type"]].objects.create(
            name=request.POST["name"], owner=user
        )
        try:
            xp = int(request.POST["xp"])
        except ValueError:
            xp = 0
        try:
            bonus = int(request.POST["bonus"])
        except ValueError:
            bonus = 0
        xp = max(xp, 0)
        bonus = max(bonus, 0)
        char.random(xp=xp, bonus_points=bonus)
        char.save()
        return redirect(char.get_absolute_url())

    def get(self, request):
        return redirect("exalted:characters:index")
