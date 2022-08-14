from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from exalted.models.characters.mortals import (
    ExMerit,
    ExMortal,
    ExSpecialty,
    Intimacy,
    MeritRating,
)


class MortalDetailView(View):
    def get(self, request, *args, **kwargs):
        char = ExMortal.objects.get(pk=kwargs["pk"])
        context = {
            "object": char,
            "merits": MeritRating.objects.filter(character=char).order_by(
                "merit__name"
            ),
            "specialties": char.specialties.all().order_by("name"),
        }
        return render(request, "exalted/characters/mortal/mortal/detail.html", context,)


class MortalCreateView(CreateView):
    model = ExMortal
    fields = "__all__"
    template_name = "exalted/characters/mortal/mortal/create.html"


class MortalUpdateView(UpdateView):
    model = ExMortal
    fields = "__all__"
    template_name = "exalted/characters/mortal/mortal/update.html"


class SpecialtyDetailView(DetailView):
    model = ExSpecialty
    template_name = "exalted/characters/mortal/specialty/detail.html"


class SpecialtyCreateView(CreateView):
    model = ExSpecialty
    fields = "__all__"
    template_name = "exalted/characters/mortal/specialty/create.html"


class SpecialtyUpdateView(UpdateView):
    model = ExSpecialty
    fields = "__all__"
    template_name = "exalted/characters/mortal/specialty/update.html"


class IntimacyDetailView(DetailView):
    model = Intimacy
    template_name = "exalted/characters/mortal/intimacy/detail.html"


class IntimacyCreateView(CreateView):
    model = Intimacy
    fields = "__all__"
    template_name = "exalted/characters/mortal/intimacy/create.html"


class IntimacyUpdateView(UpdateView):
    model = Intimacy
    fields = "__all__"
    template_name = "exalted/characters/mortal/intimacy/update.html"


class MeritDetailView(DetailView):
    model = ExMerit
    template_name = "exalted/characters/mortal/merit/detail.html"


class MeritCreateView(CreateView):
    model = ExMerit
    fields = "__all__"
    template_name = "exalted/characters/mortal/merit/create.html"


class MeritUpdateView(UpdateView):
    model = ExMerit
    fields = "__all__"
    template_name = "exalted/characters/mortal/merit/update.html"
