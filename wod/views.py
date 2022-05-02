from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from wod.forms import MageForm
from wod.models import Character, Mage, MageFaction


# Create your views here.



class MageCreateView(CreateView):
    """Class that manages the Mage Create view"""

    model = Mage
    form_class = MageForm
    template_name = "characters/mage/create.html"


class MageDetailView(DetailView):
    """Class that manages Views for mages"""

    model = Mage
    template_name = "characters/mage/detail.html"


class MageUpdate(UpdateView):
    """Class that manages the Mage Update view"""

    model = Mage
    fields = "__all__"
    template_name = "characters/mage/update.html"


def load_factions(request):
    affiliation_id = request.GET.get("affiliation")
    factions = MageFaction.objects.filter(parent=affiliation_id).order_by("name")
    return render(
        request,
        "characters/mage/load_faction_dropdown_list.html",
        {"factions": factions},
    )


def load_subfactions(request):
    faction_id = request.GET.get("faction")
    subfactions = MageFaction.objects.filter(parent=faction_id).order_by("name")
    return render(
        request,
        "characters/mage/load_subfaction_dropdown_list.html",
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
        return redirect("characters_index")
