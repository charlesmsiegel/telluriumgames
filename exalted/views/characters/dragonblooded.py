# from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from exalted.models.characters.charms import DragonBloodedCharm

# from exalted.forms import (
#     ExaltedAbilitiesForm,
#     ExaltedAttributeForm,
#     ExaltedCharmForm,
#     ExaltedIntimacyForm,
#     ExaltedMeritsForm,
#     SolarCreationForm,
# )
# from exalted.models.characters.mortals import (
#     ExMerit,
#     ExSpecialty,
#     Intimacy,
#     MeritRating,
# )
from exalted.models.characters.dragonblooded import DragonBlooded

#     Charm,
#     MartialArtsCharm,
#     MartialArtsStyle,
#     SolarCharm,
# )
# from exalted.models.characters.utils import ABILITIES
# from game.models import Chronicle


class DragonBloodedDetailView(View):
    def get(self, request, *args, **kwargs):
        char = DragonBlooded.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)
        return render(
            request,
            "exalted/characters/dragonblooded/dragonblooded/detail.html",
            context,
        )


#     def get_context(self, char):
#         return {
#             "object": char,
#             "merits": MeritRating.objects.filter(character=char).order_by(
#                 "merit__name"
#             ),
#             "specialties": char.specialties.all().order_by("name"),
#         }


class DragonBloodedCreateView(CreateView):
    model = DragonBlooded
    fields = "__all__"
    template_name = "exalted/characters/dragonblooded/dragonblooded/form.html"


class DragonBloodedUpdateView(UpdateView):
    model = DragonBlooded
    fields = "__all__"
    template_name = "exalted/characters/dragonblooded/dragonblooded/form.html"


class DragonBloodedCharmDetailView(DetailView):
    model = DragonBloodedCharm
    template_name = "exalted/characters/dragonblooded/dragonbloodedcharm/detail.html"


class DragonBloodedCharmCreateView(CreateView):
    model = DragonBloodedCharm
    fields = "__all__"
    template_name = "exalted/characters/dragonblooded/dragonbloodedcharm/form.html"


class DragonBloodedCharmUpdateView(UpdateView):
    model = DragonBloodedCharm
    fields = "__all__"
    template_name = "exalted/characters/dragonblooded/dragonbloodedcharm/form.html"
