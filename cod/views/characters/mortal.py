from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from cod.models.characters.mortal import (
    Condition,
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
        return render(request, "cod/characters/mortal/mortal/detail.html", context,)


class MortalCreateView(CreateView):
    model = Mortal
    fields = "__all__"
    template_name = "cod/characters/mortal/mortal/create.html"


class MortalUpdateView(UpdateView):
    model = Mortal
    fields = "__all__"
    template_name = "cod/characters/mortal/mortal/update.html"


class ConditionDetailView(DetailView):
    model = Condition
    template_name = "cod/characters/mortal/condition/detail.html"


class ConditionCreateView(CreateView):
    model = Condition
    fields = "__all__"
    template_name = "cod/characters/mortal/condition/create.html"


class ConditionUpdateView(UpdateView):
    model = Condition
    fields = "__all__"
    template_name = "cod/characters/mortal/condition/update.html"


class MeritDetailView(DetailView):
    model = Merit
    template_name = "cod/characters/mortal/merit/detail.html"


class MeritCreateView(CreateView):
    model = Merit
    fields = "__all__"
    template_name = "cod/characters/mortal/merit/create.html"


class MeritUpdateView(UpdateView):
    model = Merit
    fields = "__all__"
    template_name = "cod/characters/mortal/merit/update.html"


class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = "cod/characters/mortal/specialty/detail.html"


class SpecialtyCreateView(CreateView):
    model = Specialty
    fields = "__all__"
    template_name = "cod/characters/mortal/specialty/create.html"


class SpecialtyUpdateView(UpdateView):
    model = Specialty
    fields = "__all__"
    template_name = "cod/characters/mortal/specialty/update.html"
