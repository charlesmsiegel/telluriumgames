from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, View

from cod.forms import RandomCharacterForm
from cod.models.characters.ephemera import Ephemera
from cod.models.characters.mage import Mage, Proximi
from cod.models.characters.mortal import Mortal

from . import ephemera, mage, mortal


class CharacterIndexView(View):
    """Class that manages the Index view"""

    def get(self, request):
        context = self.get_context()
        return render(request, "cod/characters/index.html", context)

    def post(self, request):
        context = self.get_context()
        return render(request, "cod/characters/index.html", context)

    def get_context(self):
        chars = Mortal.objects.all().order_by("name")
        context = {}
        context["chars"] = chars
        context["ephemera"] = Ephemera.objects.all().order_by("name")
        context["form"] = RandomCharacterForm
        return context


class GenericCharacterDetailView(View):
    """Class that manages Views for characters"""

    create_views = {
        "mortal": mortal.MortalDetailView,
        "mage": mage.MageDetailView,
        "proximi": mage.ProximiDetailView,
    }

    def get(self, request, *args, **kwargs):
        char = Mortal.objects.get(pk=kwargs["pk"])
        if char.type in self.create_views:
            return self.create_views[char.type].as_view()(request, *args, **kwargs)
        return redirect("cod:characters:index")


def load_character_types(request):
    characters = {
        "core": ["mortal"],
        "mage": ["mage", "proximi"],
    }
    gameline = request.GET.get("gameline")
    character_types = characters[gameline]
    return render(
        request,
        "cod/characters/load_character_dropdown_list.html",
        {"character_types": character_types},
    )


class RandomCharacterView(View):
    chars = {
        "mortal": Mortal,
        "mage": Mage,
        "proximi": Proximi,
    }

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        char = self.chars[request.POST["char_type"]].objects.create(
            name=request.POST["char_name"], owner=user
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
