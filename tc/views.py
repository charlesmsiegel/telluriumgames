from django.shortcuts import render, redirect
from django.views.generic import View

from tc.models.character.human import Human
from tc.models.character.talent import Talent
from tc.models.character.aberrant import Aberrant

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
        return {
            "character": char
        }

class TalentDetailView(View):
    def get(self, request, pk):
        context = self.get_context(pk)
        return render(request, "tc/characters/talent/detail.html", context)

    def get_context(self, pk):
        char = Talent.objects.get(id=pk)
        return {
            "character": char
        }

class AberrantDetailView(View):
    def get(self, request, pk):
        context = self.get_context(pk)
        return render(request, "tc/characters/aberrant/detail.html", context)

    def get_context(self, pk):
        char = Aberrant.objects.get(id=pk)
        return {
            "character": char
        }

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
