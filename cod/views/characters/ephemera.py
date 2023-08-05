from collections import namedtuple

from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from cod.models.characters.ephemera import Ephemera, Numina


class EphemeraDetailView(DetailView):
    model = Ephemera
    template_name = "cod/characters/ephemera/ephemera/detail.html"


class EphemeraCreateView(CreateView):
    model = Ephemera
    fields = "__all__"
    template_name = "cod/characters/ephemera/ephemera/form.html"


class EphemeraUpdateView(UpdateView):
    model = Ephemera
    fields = "__all__"
    template_name = "cod/characters/ephemera/ephemera/form.html"


class NuminaDetailView(DetailView):
    model = Numina
    template_name = "cod/characters/ephemera/numina/detail.html"


class NuminaCreateView(CreateView):
    model = Numina
    fields = "__all__"
    template_name = "cod/characters/ephemera/numina/form.html"


class NuminaUpdateView(UpdateView):
    model = Numina
    fields = "__all__"
    template_name = "cod/characters/ephemera/numina/form.html"
