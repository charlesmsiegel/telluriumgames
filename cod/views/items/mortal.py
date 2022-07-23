from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView

from cod.models.items.mortal import Equipment, Item


class ItemDetailView(DetailView):
    model = Item
    template_name = "cod/items/mortal/item/detail.html"


class ItemCreateView(CreateView):
    model = Item
    fields = "__all__"
    template_name = "cod/items/mortal/item/create.html"


class ItemUpdateView(UpdateView):
    model = Item
    fields = "__all__"
    template_name = "cod/items/mortal/item/update.html"


class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = "cod/items/mortal/equipment/detail.html"


class EquipmentCreateView(CreateView):
    model = Equipment
    fields = "__all__"
    template_name = "cod/items/mortal/equipment/create.html"


class EquipmentUpdateView(UpdateView):
    model = Equipment
    fields = "__all__"
    template_name = "cod/items/mortal/equipment/update.html"
