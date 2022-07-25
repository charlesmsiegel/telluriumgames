from django.shortcuts import redirect, render
from django.views.generic import View

from wod.models.items.human import Item
from wod.models.items.mage import Grimoire
from wod.forms import RandomItemForm

from . import human, mage, werewolf


class ItemIndexView(View):
    def get(self, request):
        context = self.get_context()
        return render(request, "wod/items/index.html", context)

    def post(self, request):
        context = self.get_context()
        return render(request, "wod/items/index.html", context)

    def get_context(self):
        items = Item.objects.all().order_by("name")
        context = {}
        context["items"] = items
        context['form'] = RandomItemForm
        return context

def load_item_types(request):
    items = {
        # "werewolf": [],
        "mage": ["grimoire"],
    }
    gameline = request.GET.get("gameline")
    item_types = items[gameline]
    return render(
        request,
        "wod/items/load_item_dropdown_list.html",
        {"item_types": item_types},
    )


class GenericItemDetailView(View):
    views = {
        "item": human.ItemDetailView,
        "wonder": mage.WonderDetailView,
        "grimoire": mage.GrimoireDetailView,
        "library": mage.LibraryDetailView,
        "fetish": werewolf.FetishDetailView,
    }

    def get(self, request, *args, **kwargs):
        item = Item.objects.get(pk=kwargs["pk"])
        if item.type in self.views:
            return self.views[item.type].as_view()(request, *args, **kwargs)
        return redirect("wod:items:index")


class RandomItemView(View):
    items = {
        "grimoire": Grimoire,
    }

    def post(self, request):
        item = self.items[request.POST["item_type"]].objects.create(
            name=request.POST["name"]
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
