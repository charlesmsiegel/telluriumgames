from django.views.generic import CreateView, DetailView, UpdateView

from wod.models.items.human import Item


class ItemDetailView(DetailView):
    model = Item
    template_name = "wod/items/human/item/detail.html"


class ItemCreateView(CreateView):
    model = Item
    fields = "__all__"
    template_name = "wod/items/human/item/create.html"


class ItemUpdateView(UpdateView):
    model = Item
    fields = "__all__"
    template_name = "wod/items/human/item/create.html"
