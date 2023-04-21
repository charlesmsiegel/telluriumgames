from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from core.views import BaseCharacterView
from exalted.models.characters.mortals import (
    ExMerit,
    ExMortal,
    ExSpecialty,
    Intimacy,
    MeritRating,
)


class MortalDetailView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        char = ExMortal.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)
        return render(request, "exalted/characters/mortal/mortal/detail.html", context,)

    def get_context(self, character):
        context = super().get_context(character)
        context["merits"] = MeritRating.objects.filter(character=character).order_by(
            "merit__name"
        )
        context["specialties"] = character.specialties.all().order_by("name")
        return context


class MortalCreateView(CreateView):
    model = ExMortal
    fields = "__all__"
    template_name = "exalted/characters/mortal/mortal/form.html"


class MortalUpdateView(UpdateView):
    model = ExMortal
    fields = "__all__"
    template_name = "exalted/characters/mortal/mortal/form.html"


class SpecialtyDetailView(DetailView):
    model = ExSpecialty
    template_name = "exalted/characters/mortal/specialty/detail.html"


class SpecialtyCreateView(CreateView):
    model = ExSpecialty
    fields = "__all__"
    template_name = "exalted/characters/mortal/specialty/form.html"


class SpecialtyUpdateView(UpdateView):
    model = ExSpecialty
    fields = "__all__"
    template_name = "exalted/characters/mortal/specialty/form.html"


class IntimacyDetailView(DetailView):
    model = Intimacy
    template_name = "exalted/characters/mortal/intimacy/detail.html"


class IntimacyCreateView(CreateView):
    model = Intimacy
    fields = "__all__"
    template_name = "exalted/characters/mortal/intimacy/form.html"


class IntimacyUpdateView(UpdateView):
    model = Intimacy
    fields = "__all__"
    template_name = "exalted/characters/mortal/intimacy/form.html"


class MeritDetailView(DetailView):
    model = ExMerit
    template_name = "exalted/characters/mortal/merit/detail.html"


class MeritCreateView(CreateView):
    model = ExMerit
    fields = "__all__"
    template_name = "exalted/characters/mortal/merit/form.html"


class MeritUpdateView(UpdateView):
    model = ExMerit
    fields = "__all__"
    template_name = "exalted/characters/mortal/merit/form.html"
