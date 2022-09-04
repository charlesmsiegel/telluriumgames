from django.views.generic import CreateView, DetailView, UpdateView, View
from wod.models.characters.changeling import (
    Changeling,
    Motley,
    Kith,
    House,
    CtDHuman,
    CtDLegacy,
)


class ChangelingDetailView(DetailView):
    model = Changeling
    template_name = "wod/characters/changeling/changeling/detail.html"


class ChangelingCreateView(CreateView):
    model = Changeling
    fields = "__all__"
    template_name = "wod/characters/changeling/changeling/form.html"


class ChangelingUpdateView(UpdateView):
    model = Changeling
    fields = "__all__"
    template_name = "wod/characters/changeling/changeling/form.html"


class LegacyDetailView(DetailView):
    model = CtDLegacy
    template_name = "wod/characters/changeling/legacy/detail.html"


class LegacyCreateView(CreateView):
    model = CtDLegacy
    fields = "__all__"
    template_name = "wod/characters/changeling/legacy/form.html"


class LegacyUpdateView(UpdateView):
    model = CtDLegacy
    fields = "__all__"
    template_name = "wod/characters/changeling/legacy/form.html"


class KithDetailView(DetailView):
    model = Kith
    template_name = "wod/characters/changeling/kith/detail.html"


class KithCreateView(CreateView):
    model = Kith
    fields = "__all__"
    template_name = "wod/characters/changeling/kith/form.html"


class KithUpdateView(UpdateView):
    model = Kith
    fields = "__all__"
    template_name = "wod/characters/changeling/kith/form.html"


class HouseDetailView(DetailView):
    model = House
    template_name = "wod/characters/changeling/house/detail.html"


class HouseCreateView(CreateView):
    model = House
    fields = "__all__"
    template_name = "wod/characters/changeling/house/form.html"


class HouseUpdateView(UpdateView):
    model = House
    fields = "__all__"
    template_name = "wod/characters/changeling/house/form.html"


class MotleyDetailView(DetailView):
    model = Motley
    template_name = "wod/characters/changeling/motley/detail.html"


class MotleyCreateView(CreateView):
    model = Motley
    fields = "__all__"
    template_name = "wod/characters/changeling/motley/form.html"


class MotleyUpdateView(UpdateView):
    model = Motley
    fields = "__all__"
    template_name = "wod/characters/changeling/motley/form.html"
