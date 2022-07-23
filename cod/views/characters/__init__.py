from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, View
from cod.models.characters.mage import Mage, Proximi

from cod.models.characters.mortal import Mortal
from . import mortal, mage


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


class RandomCharacterView(View):
    chars = {
        "mortal": Mortal,
        "mage": Mage,
        "proximi": Proximi,
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

