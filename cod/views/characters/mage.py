from collections import namedtuple

from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from cod.models.characters.mage import (
    Attainment,
    CoDRote,
    Legacy,
    Mage,
    Order,
    Path,
    Proximi,
    ProximiFamily,
)
from cod.models.characters.mortal import MeritRating
from core.views import BaseCharacterView

EmptyRote = namedtuple("EmptyRote", ["name", "arcana", "level"])
empty_rote = EmptyRote("", "", "")


class ProximiDetailView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        char = Proximi.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)
        return render(request, "cod/characters/mage/proximi/detail.html", context,)

    def get_context(self, character):
        context = super().get_context(character)
        context["merits"] = MeritRating.objects.filter(character=character).order_by(
            "merit__name"
        )
        context["specialties"] = character.specialties.all().order_by("name")
        all_blessings = list(context["object"].blessings.all())
        row_length = 2
        all_blessings = [
            all_blessings[i : i + row_length]
            for i in range(0, len(all_blessings), row_length)
        ]
        if len(all_blessings) != 0:
            while len(all_blessings[-1]) < row_length:
                all_blessings[-1].append(empty_rote)
        context["blessings"] = all_blessings
        return context


class ProximiCreateView(CreateView):
    model = Proximi
    fields = "__all__"
    template_name = "cod/characters/mage/proximi/form.html"


class ProximiUpdateView(UpdateView):
    model = Proximi
    fields = "__all__"
    template_name = "cod/characters/mage/proximi/form.html"


class MageDetailView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        char = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)

        return render(request, "cod/characters/mage/mage/detail.html", context,)

    def get_context(self, character):
        context = super().get_context(character)

        context["merits"] = MeritRating.objects.filter(character=character).order_by(
            "merit__name"
        )

        context["specialties"] = (character.specialties.all().order_by("name"),)

        all_rotes = list(context["object"].rotes.all())
        row_length = 2
        all_rotes = [
            all_rotes[i : i + row_length] for i in range(0, len(all_rotes), row_length)
        ]
        if len(all_rotes) != 0:
            while len(all_rotes[-1]) < row_length:
                all_rotes[-1].append(empty_rote)
        context["rotes"] = all_rotes

        all_praxes = list(context["object"].praxes.all())
        row_length = 2
        all_praxes = [
            all_praxes[i : i + row_length]
            for i in range(0, len(all_praxes), row_length)
        ]
        if len(all_praxes) != 0:
            while len(all_praxes[-1]) < row_length:
                all_praxes[-1].append(empty_rote)
        context["praxes"] = all_praxes

        return context


class MageCreateView(CreateView):
    model = Mage
    fields = "__all__"
    template_name = "cod/characters/mage/mage/form.html"


class MageUpdateView(UpdateView):
    model = Mage
    fields = "__all__"
    template_name = "cod/characters/mage/mage/form.html"


class ProximiFamilyDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        fam = ProximiFamily.objects.get(pk=kwargs["pk"])
        context = {
            "object": fam,
        }
        context["arcana"] = ", ".join(
            [x.title() for x in fam.path.ruling_arcana + [fam.blessing_arcana]]
        )

        all_blessings = list(
            context["object"].possible_blessings.all().order_by("arcanum")
        )
        row_length = 2
        all_blessings = [
            all_blessings[i : i + row_length]
            for i in range(0, len(all_blessings), row_length)
        ]
        if len(all_blessings) != 0:
            while len(all_blessings[-1]) < row_length:
                all_blessings[-1].append(empty_rote)
        context["blessings"] = all_blessings
        return render(
            request, "cod/characters/mage/proximifamily/detail.html", context,
        )


class ProximiFamilyCreateView(CreateView):
    model = ProximiFamily
    fields = "__all__"
    template_name = "cod/characters/mage/proximifamily/form.html"


class ProximiFamilyUpdateView(UpdateView):
    model = ProximiFamily
    fields = "__all__"
    template_name = "cod/characters/mage/proximifamily/form.html"


class LegacyDetailView(DetailView):
    model = Legacy
    template_name = "cod/characters/mage/legacy/detail.html"


class LegacyCreateView(CreateView):
    model = Legacy
    fields = "__all__"
    template_name = "cod/characters/mage/legacy/form.html"


class LegacyUpdateView(UpdateView):
    model = Legacy
    fields = "__all__"
    template_name = "cod/characters/mage/legacy/form.html"


class OrderDetailView(DetailView):
    model = Order
    template_name = "cod/characters/mage/order/detail.html"


class OrderCreateView(CreateView):
    model = Order
    fields = "__all__"
    template_name = "cod/characters/mage/order/form.html"


class OrderUpdateView(UpdateView):
    model = Order
    fields = "__all__"
    template_name = "cod/characters/mage/order/form.html"


class PathDetailView(DetailView):
    model = Path
    template_name = "cod/characters/mage/path/detail.html"


class PathCreateView(CreateView):
    model = Path
    fields = "__all__"
    template_name = "cod/characters/mage/path/form.html"


class PathUpdateView(UpdateView):
    model = Path
    fields = "__all__"
    template_name = "cod/characters/mage/path/form.html"


class RoteDetailView(DetailView):
    model = CoDRote
    template_name = "cod/characters/mage/rote/detail.html"


class RoteCreateView(CreateView):
    model = CoDRote
    fields = "__all__"
    template_name = "cod/characters/mage/rote/form.html"


class RoteUpdateView(UpdateView):
    model = CoDRote
    fields = "__all__"
    template_name = "cod/characters/mage/rote/form.html"


class AttainmentDetailView(DetailView):
    model = Attainment
    template_name = "cod/characters/mage/attainment/detail.html"


class AttainmentCreateView(CreateView):
    model = Attainment
    fields = "__all__"
    template_name = "cod/characters/mage/attainment/form.html"


class AttainmentUpdateView(UpdateView):
    model = Attainment
    fields = "__all__"
    template_name = "cod/characters/mage/attainment/form.html"
