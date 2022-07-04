from django.shortcuts import render, redirect
from django.views.generic import View, DetailView

from exalted.models.characters.mortals import Mortal

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

class MortalDetailView(DetailView):
    model = Mortal
    template = "exalted/characters/mortal/detail.html"

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
            name=request.POST["char_name"], player=request.user.cod_profile
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
