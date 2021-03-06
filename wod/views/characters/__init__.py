from django.shortcuts import redirect, render
from django.views.generic import View

from wod.forms import RandomCharacterForm
from wod.models.characters.human import Character, Group
from wod.models.characters.mage.mage import Cabal, Mage
from wod.models.characters.werewolf.garou import Pack, Werewolf

from . import human, mage, werewolf


class CharacterIndexView(View):
    def get(self, request):
        context = self.get_context()
        return render(request, "wod/characters/index.html", context)

    def post(self, request):
        context = self.get_context()
        return render(request, "wod/characters/index.html", context)

    def get_context(self):
        characters = Character.objects.all().order_by("name")
        context = {}
        context["characters"] = characters
        context["form"] = RandomCharacterForm
        context["groups"] = Group.objects.all().order_by("name")
        return context


def load_character_types(request):
    characters = {
        "werewolf": ["werewolf", "pack"],
        "mage": ["mage", "cabal"],
    }
    gameline = request.GET.get("gameline")
    character_types = characters[gameline]
    return render(
        request,
        "wod/characters/load_character_dropdown_list.html",
        {"character_types": character_types},
    )


class GenericCharacterDetailView(View):
    character_views = {
        "character": human.CharacterDetailView,
        "human": human.HumanDetailView,
        "garou": werewolf.WerewolfDetailView,
        "mage": mage.MageDetailView,
        "spirit_character": werewolf.SpiritDetailView,
    }

    def get(self, request, *args, **kwargs):
        char = Character.objects.get(pk=kwargs["pk"])
        if char.type in self.character_views:
            return self.character_views[char.type].as_view()(request, *args, **kwargs)
        return redirect("wod:characters:index")


class RandomCharacterView(View):
    chars = {
        "werewolf": Werewolf,
        "mage": Mage,
        "cabal": Cabal,
        "pack": Pack,
    }

    def post(self, request, *args, **kwargs):
        if request.POST["character_type"] in ["werewolf", "mage"]:
            char = self.chars[request.POST["character_type"]].objects.create(
                name=request.POST["character_name"], player=request.user
            )
        else:
            char = self.chars[request.POST["character_type"]].objects.create(
                name=request.POST["character_name"]
            )
        try:
            freebies = int(request.POST["freebies"])
        except ValueError:
            freebies = 15
        try:
            xp = int(request.POST["xp"])
        except ValueError:
            xp = 0
        xp = max(xp, 0)
        freebies = max(freebies, 0)
        char.random(freebies=freebies, xp=xp)
        char.save()
        return redirect(char.get_absolute_url())

    def get(self, request):
        return redirect("wod:characters:index")


class GenericGroupDetailView(View):
    group_views = {
        "group": human.GroupDetailView,
        "cabal": mage.CabalDetailView,
        "pack": werewolf.PackDetailView,
    }

    def get(self, request, *args, **kwargs):
        group = Group.objects.get(pk=kwargs["pk"])
        if group.type in self.group_views:
            return self.group_views[group.type].as_view()(request, *args, **kwargs)
        return redirect("wod:characters:index")
