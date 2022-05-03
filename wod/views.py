from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from wod.forms import MageForm
from wod.models import Character, Mage, MageFaction


# Create your views here.
class IndexView(View):
    """Class that manages the Index view"""

    def get(self, request):
        context = self.get_context()
        return render(request, "wod/characters/index.html", context)

    def post(self, request):
        context = self.get_context()
        # character_class_dict = {
        #     # "vampire": Vampire,
        #     # "werewolf": Werewolf,
        #     "mage": Mage,
        #     # "wraith": Wraith,
        #     # "changeling": Changeling,
        # }
        # if request.POST["character_type"] in character_class_dict:
        #     char_cl = character_class_dict[request.POST["character_type"]]
        #     character = char_cl.objects.create(
        #         name=request.POST["character_name"], player=request.user
        #     )
        #     return redirect(character.get_absolute_url())
        return render(request, "wod/characters/index.html", context)

    def get_context(self):
        chars = Character.objects.all().order_by("name")
        context = {}
        context["chars"] = chars


class MageCreateView(CreateView):
    """Class that manages the Mage Create view"""

    model = Mage
    form_class = MageForm
    template_name = "wod/characters/mage/create.html"


class MageDetailView(DetailView):
    """Class that manages Views for mages"""

    model = Mage
    template_name = "wod/characters/mage/detail.html"


class MageUpdate(UpdateView):
    """Class that manages the Mage Update view"""

    model = Mage
    fields = "__all__"
    template_name = "wod/characters/mage/update.html"


def load_factions(request):
    affiliation_id = request.GET.get("affiliation")
    factions = MageFaction.objects.filter(parent=affiliation_id).order_by("name")
    return render(
        request,
        "wod/characters/mage/load_faction_dropdown_list.html",
        {"factions": factions},
    )


def load_subfactions(request):
    faction_id = request.GET.get("faction")
    subfactions = MageFaction.objects.filter(parent=faction_id).order_by("name")
    return render(
        request,
        "wod/characters/mage/load_subfaction_dropdown_list.html",
        {"subfactions": subfactions},
    )


class CharacterDetailView(View):
    """Class that manages Views for characters"""

    create_views = {
        # "vampire": VampireView,
        # "werewolf": WerewolfView,
        "mage": MageDetailView,
        # "changeling": ChangelingView,
        # "wraith": WraithView,
    }

    def get(self, request, *args, **kwargs):
        char = Character.objects.get(pk=kwargs["pk"])
        if char.type in self.create_views:
            return self.create_views[char.type].as_view()(request, *args, **kwargs)
        return redirect("wod:characters_index")
