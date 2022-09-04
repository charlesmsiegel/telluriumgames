from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, View

from wod.models.characters.changeling import (
    Changeling,
    CtDHuman,
    CtDLegacy,
    House,
    Kith,
    Motley,
)
from wod.models.characters.human import MeritFlawRating


class ChangelingDetailView(View):
    def get(self, request, *args, **kwargs):
        changeling = Changeling.objects.get(pk=kwargs["pk"])
        context = self.get_context(changeling)
        return render(
            request, "wod/characters/changeling/changeling/detail.html", context
        )

    def get_context(self, changeling):
        context = {"object": changeling}
        specialties = {}
        for attribute in changeling.get_attributes():
            specialties[attribute] = ", ".join(
                [x.name for x in changeling.specialties.filter(stat=attribute)]
            )
        for ability in changeling.get_abilities():
            specialties[ability] = ", ".join(
                [x.name for x in changeling.specialties.filter(stat=ability)]
            )
        for key, value in specialties.items():
            context[f"{key}_spec"] = value

        context["merits_and_flaws"] = MeritFlawRating.objects.order_by(
            "mf__name"
        ).filter(character=changeling)

        return context


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
