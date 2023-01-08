from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, View

from cod.models.items.mortal import Item

from . import mortal


class ItemIndexView(View):
    """Class that manages the Index view"""

    def get(self, request):
        context = self.get_context()
        return render(request, "cod/items/index.html", context)

    def post(self, request):
        context = self.get_context()
        return render(request, "cod/items/index.html", context)

    def get_context(self):
        items = Item.objects.filter(chronicle=None).order_by("name")
        context = {}
        context["items"] = items
        return context


class GenericItemDetailView(View):
    create_views = {
        "item": mortal.ItemDetailView,
        "equipment": mortal.EquipmentDetailView,
    }

    def get(self, request, *args, **kwargs):
        item = Item.objects.get(pk=kwargs["pk"])
        if item.type in self.create_views:
            return self.create_views[item.type].as_view()(request, *args, **kwargs)
        return redirect("cod:items:index")
