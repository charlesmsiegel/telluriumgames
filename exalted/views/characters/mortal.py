from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, View, UpdateView

from exalted.models.characters.mortals import (
    Intimacy,
    Merit,
    MeritRating,
    Mortal,
    Specialty,
)


class MortalDetailView(View):
    def get(self, request, *args, **kwargs):
        char = Mortal.objects.get(pk=kwargs["pk"])
        context = {
            "object": char,
            "merits": MeritRating.objects.filter(character=char).order_by(
                "merit__name"
            ),
            "specialties": char.specialties.all().order_by("name"),
        }
        return render(
            request, "exalted/characters/exalted/mortal/detail.html", context,
        )


class MortalCreateView(CreateView):
    model = Mortal
    fields = "__all__"
    template_name = "exalted/characters/exalted/mortal/create.html"


class MortalUpdateView(UpdateView):
    model = Mortal
    fields = "__all__"
    template_name = "exalted/characters/exalted/mortal/update.html"


class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = "exalted/characters/exalted/specialty/detail.html"


class SpecialtyCreateView(CreateView):
    model = Specialty
    fields = "__all__"
    template_name = "exalted/characters/exalted/specialty/create.html"


class SpecialtyUpdateView(UpdateView):
    model = Specialty
    fields = "__all__"
    template_name = "exalted/characters/exalted/specialty/update.html"


class IntimacyDetailView(DetailView):
    model = Intimacy
    template_name = "exalted/characters/exalted/intimacy/detail.html"


class IntimacyCreateView(CreateView):
    model = Intimacy
    fields = "__all__"
    template_name = "exalted/characters/exalted/intimacy/create.html"


class IntimacyUpdateView(UpdateView):
    model = Intimacy
    fields = "__all__"
    template_name = "exalted/characters/exalted/intimacy/update.html"


class MeritDetailView(DetailView):
    model = Merit
    template_name = "exalted/characters/exalted/merit/detail.html"


class MeritCreateView(CreateView):
    model = Merit
    fields = "__all__"
    template_name = "exalted/characters/exalted/merit/create.html"


class MeritUpdateView(UpdateView):
    model = Merit
    fields = "__all__"
    template_name = "exalted/characters/exalted/merit/update.html"
