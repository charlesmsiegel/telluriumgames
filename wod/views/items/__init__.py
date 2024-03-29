from django.shortcuts import redirect, render
from django.views.generic import View

from wod.forms.items import RandomItemForm
from wod.models.items.human import WoDItem
from wod.models.items.mage import Artifact, Charm, Grimoire, Talisman

from . import human, mage, werewolf


class ItemIndexView(View):
    def get(self, request):
        context = self.get_context()
        return render(request, "wod/items/index.html", context)

    def post(self, request):
        context = self.get_context()
        return render(request, "wod/items/index.html", context)

    def get_context(self):
        items = WoDItem.objects.filter(chronicle=None).order_by("name")
        context = {}
        context["items"] = items
        context["form"] = RandomItemForm
        return context


def load_item_types(request):
    items = {
        # "werewolf": [],
        "mage": ["charm", "artifact", "talisman", "grimoire"],
    }
    gameline = request.GET.get("gameline")
    item_types = items[gameline]
    return render(
        request, "wod/items/load_item_dropdown_list.html", {"item_types": item_types},
    )


class GenericItemDetailView(View):
    views = {
        "item": human.ItemDetailView,
        "wonder": mage.WonderDetailView,
        "grimoire": mage.GrimoireDetailView,
        "fetish": werewolf.FetishDetailView,
        "charm": mage.CharmDetailView,
        "artifact": mage.ArtifactDetailView,
        "talisman": mage.TalismanDetailView,
        "weapon": human.WeaponDetailView,
        "melee_weapon": human.MeleeWeaponDetailView,
        "thrown_weapon": human.ThrownWeaponDetailView,
        "ranged_weapon": human.RangedWeaponDetailView,
    }

    def get(self, request, *args, **kwargs):
        item = WoDItem.objects.get(pk=kwargs["pk"])
        if item.type in self.views:
            return self.views[item.type].as_view()(request, *args, **kwargs)
        return redirect("wod:items:index")


class RandomItemView(View):
    items = {
        "grimoire": Grimoire,
        "charm": Charm,
        "artifact": Artifact,
        "talisman": Talisman,
    }

    def post(self, request):
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        item = self.items[request.POST["item_type"]].objects.create(
            name=request.POST["name"], owner=user
        )
        if request.POST["rank"] is None:
            rank = None
        else:
            rank = int(request.POST["rank"])
        item.random(rank=rank)
        item.save()
        return redirect(item.get_absolute_url())

    def get(self, request):
        return redirect("wod:items:index")
