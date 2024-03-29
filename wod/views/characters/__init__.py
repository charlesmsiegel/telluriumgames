from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import View

from wod.forms.characters import CreateCharacterForm, RandomCharacterForm
from wod.models.characters.changeling import Changeling, Motley
from wod.models.characters.human import Character, Group
from wod.models.characters.mage.cabal import Cabal
from wod.models.characters.mage.mage import Mage
from wod.models.characters.werewolf import Fomor, Kinfolk, Pack, Werewolf

from . import changeling, human, mage, werewolf


class RandomCharacterView(View):
    chars = {
        "kinfolk": Kinfolk,
        "werewolf": Werewolf,
        "mage": Mage,
        "cabal": Cabal,
        "pack": Pack,
        "fomor": Fomor,
        "changeling": Changeling,
        "motley": Motley,
    }

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        if request.POST["character_type"] in [
            "werewolf",
            "mage",
            "kinfolk",
            "fomor",
            "changeling",
        ]:
            char = self.chars[request.POST["character_type"]].objects.create(
                name="", owner=user
            )
        else:
            char = self.chars[request.POST["character_type"]].objects.create(name="")

        xp = 0
        freebies = 15
        char.random(freebies=freebies, xp=xp)
        char.save()
        messages.success(request, "Character Created!")
        # messages.error(request, "Character Not Created")
        return redirect(char.get_absolute_url())

    def get(self, request):
        return redirect("wod:characters:index")


class CharacterIndexView(View):
    def get(self, request):
        context = self.get_context()
        return render(request, "wod/characters/index.html", context)

    def post(self, request, *args, **kwargs):
        random_list = ["pack", "kinfolk", "fomor", "changeling", "cabal", "motley"]
        context = self.get_context()
        form = CreateCharacterForm(request.POST)
        if "character_type" in form.data:
            if form.data["character_type"] in random_list:
                return RandomCharacterView.as_view()(request, *args, **kwargs)
            return redirect(
                f"wod:characters:{form.data['gameline']}:create_{form.data['character_type']}"
            )
        return render(request, "wod/characters/index.html", context)

    def get_context(self):
        characters = Character.objects.filter(chronicle=None).order_by("name")
        context = {}
        context["characters"] = characters
        context["form"] = CreateCharacterForm()
        context["groups"] = Group.objects.filter(chronicle=None).order_by("name")
        return context


def load_character_types(request):
    characters = {
        # "vampire": ["vampire", "ghoul", "coterie"],
        "werewolf": ["werewolf", "pack", "kinfolk", "fomor"],
        "mage": ["mage", "cabal"],  # "sorcerer", "familiar"
        # "wraith": ["wraith", "circle"],
        "changeling": ["changeling", "motley"],
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
        "kinfolk": werewolf.KinfolkDetailView,
        "garou": werewolf.WerewolfDetailView,
        "mage": mage.MageDetailView,
        "spirit_character": werewolf.SpiritDetailView,
        "fomor": werewolf.FomorDetailView,
        "changeling": changeling.ChangelingDetailView,
        "mta_human": mage.MtAHumanView,
    }

    def get(self, request, *args, **kwargs):
        char = Character.objects.get(pk=kwargs["pk"])
        if char.type in self.character_views:
            return self.character_views[char.type].as_view()(request, *args, **kwargs)
        return redirect("wod:characters:index")

    def post(self, request, *args, **kwargs):
        char = Character.objects.get(pk=kwargs["pk"])
        if char.type in self.character_views:
            return self.character_views[char.type].as_view()(request, *args, **kwargs)
        return redirect("wod:characters:index")


class GenericGroupDetailView(View):
    group_views = {
        "group": human.GroupDetailView,
        "cabal": mage.CabalDetailView,
        "pack": werewolf.PackDetailView,
        "motley": changeling.MotleyDetailView,
    }

    def get(self, request, *args, **kwargs):
        group = Group.objects.get(pk=kwargs["pk"])
        if group.type in self.group_views:
            return self.group_views[group.type].as_view()(request, *args, **kwargs)
        return redirect("wod:characters:index")
