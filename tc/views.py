from django.shortcuts import redirect, render
from django.views.generic import View

from tc.models.characters.aberrant import Aberrant
from tc.models.characters.human import Human
from tc.models.characters.talent import Talent


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
        return {"character": char}


class TalentDetailView(View):
    def get(self, request, pk):
        context = self.get_context(pk)
        return render(request, "tc/characters/talent/detail.html", context)

    def get_context(self, pk):
        char = Talent.objects.get(id=pk)
        return {"character": char}


class AberrantDetailView(View):
    def get(self, request, pk):
        context = self.get_context(pk)
        return render(request, "tc/characters/aberrant/detail.html", context)

    def get_context(self, pk):
        char = Aberrant.objects.get(id=pk)
        return {"character": char}


class CharacterDetailView(View):
    create_views = {
        "human": HumanDetailView,
        "talent": TalentDetailView,
        "aberrant": AberrantDetailView,
    }

    def get(self, request, *args, **kwargs):
        char = Human.objects.get(pk=kwargs["pk"])
        if char.type in self.create_views:
            return self.create_views[char.type].as_view()(request, *args, **kwargs)
        return redirect("tc:characters_index")

class RandomCharacterView(View):
    chars = {
        "human": Human,
        "talent": Talent,
        "aberrant": Aberrant,
    }

    def post(self, request, *args, **kwargs):
        char = self.chars[request.POST["char_type"]].objects.create(
            name=request.POST["char_name"], player=request.user.tc_profile
        )
        char.random(xp=int(request.POST["xp"]))
        char.save()
        return redirect(char.get_absolute_url())

    def get(self, request):
        return redirect("cod:characters_index")
