from django.views.generic import DetailView, CreateView, UpdateView

from wod.models.items.werewolf import Fetish


class FetishDetailView(DetailView):
    model = Fetish
    template_name = "wod/items/werewolf/fetish/detail.html"


class FetishCreateView(CreateView):
    model = Fetish
    fields = "__all__"
    template_name = "wod/items/werewolf/fetish/create.html"


class FetishUpdateView(UpdateView):
    model = Fetish
    fields = "__all__"
    template_name = "wod/items/werewolf/fetish/update.html"
