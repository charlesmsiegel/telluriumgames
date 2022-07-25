from django.shortcuts import redirect, render
from django.views.generic import View

from tc.forms import RandomCharacterForm
from tc.models.characters.aberrant import Aberrant
from tc.models.characters.human import Human
from tc.models.characters.talent import Talent

from . import aberrant, human, talent


class IndexView(View):
    """Class that manages the Index view"""

    def get(self, request):
        context = self.get_context()
        return render(request, "tc/characters/index.html", context)

    def get_context(self):
        chars = Human.objects.all().order_by("name")
        context = {}
        context["chars"] = chars
        context["form"] = RandomCharacterForm
        return context


def load_character_types(request):
    characters = {
        "core": ["human", "talent"],
        "aberrant": ["aberrant"],
    }
    gameline = request.GET.get("gameline")
    character_types = characters[gameline]
    return render(
        request,
        "tc/characters/load_character_dropdown_list.html",
        {"character_types": character_types},
    )


class CharacterDetailView(View):
    detail_views = {
        "human": human.HumanDetailView,
        "talent": talent.TalentDetailView,
        "aberrant": aberrant.AberrantDetailView,
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
