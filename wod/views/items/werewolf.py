from django.views.generic import CreateView, DetailView, UpdateView

from wod.models.items.werewolf import Fetish


class FetishDetailView(DetailView):
    model = Fetish
    template_name = "wod/items/werewolf/fetish/detail.html"


class FetishCreateView(CreateView):
    model = Fetish
    fields = "__all__"
    template_name = "wod/items/werewolf/fetish/form.html"


class FetishUpdateView(UpdateView):
    model = Fetish
    fields = "__all__"
    template_name = "wod/items/werewolf/fetish/form.html"
