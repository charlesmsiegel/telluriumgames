from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from cod.models.characters.mortal import (
    CoDMerit,
    CoDSpecialty,
    Condition,
    MeritRating,
    Mortal,
    Tilt,
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
            request,
            "cod/characters/mortal/mortal/detail.html",
            context,
        )


class MortalCreateView(CreateView):
    model = Mortal
    fields = "__all__"
    template_name = "cod/characters/mortal/mortal/form.html"


class MortalUpdateView(UpdateView):
    model = Mortal
    fields = "__all__"
    template_name = "cod/characters/mortal/mortal/form.html"


class ConditionDetailView(DetailView):
    model = Condition
    template_name = "cod/characters/mortal/condition/detail.html"


class ConditionCreateView(CreateView):
    model = Condition
    fields = "__all__"
    template_name = "cod/characters/mortal/condition/form.html"


class ConditionUpdateView(UpdateView):
    model = Condition
    fields = "__all__"
    template_name = "cod/characters/mortal/condition/form.html"


class MeritDetailView(DetailView):
    model = CoDMerit
    template_name = "cod/characters/mortal/merit/detail.html"


class MeritCreateView(CreateView):
    model = CoDMerit
    fields = "__all__"
    template_name = "cod/characters/mortal/merit/form.html"


class MeritUpdateView(UpdateView):
    model = CoDMerit
    fields = "__all__"
    template_name = "cod/characters/mortal/merit/form.html"


class SpecialtyDetailView(DetailView):
    model = CoDSpecialty
    template_name = "cod/characters/mortal/specialty/detail.html"


class SpecialtyCreateView(CreateView):
    model = CoDSpecialty
    fields = "__all__"
    template_name = "cod/characters/mortal/specialty/form.html"


class SpecialtyUpdateView(UpdateView):
    model = CoDSpecialty
    fields = "__all__"
    template_name = "cod/characters/mortal/specialty/form.html"


class TiltDetailView(DetailView):
    model = Tilt
    template_name = "cod/characters/mortal/tilt/detail.html"


class TiltCreateView(CreateView):
    model = Tilt
    fields = "__all__"
    template_name = "cod/characters/mortal/tilt/form.html"


class TiltUpdateView(UpdateView):
    model = Tilt
    fields = "__all__"
    template_name = "cod/characters/mortal/tilt/form.html"
