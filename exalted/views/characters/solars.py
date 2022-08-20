from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from exalted.models.characters.mortals import MeritRating
from exalted.models.characters.solars import Solar, SolarCharm


class SolarDetailView(View):
    def get(self, request, *args, **kwargs):
        char = Solar.objects.get(pk=kwargs["pk"])
        context = {
            "object": char,
            "merits": MeritRating.objects.filter(character=char).order_by(
                "merit__name"
            ),
            "specialties": char.specialties.all().order_by("name"),
        }
        return render(request, "exalted/characters/solars/solar/detail.html", context,)


class SolarCreateView(CreateView):
    model = Solar
    fields = "__all__"
    template_name = "exalted/characters/solars/solar/create.html"


class SolarUpdateView(UpdateView):
    model = Solar
    fields = "__all__"
    template_name = "exalted/characters/solars/solar/update.html"


class SolarCharmDetailView(DetailView):
    model = SolarCharm
    template_name = "exalted/characters/solars/solarcharm/detail.html"


class SolarCharmCreateView(CreateView):
    model = SolarCharm
    fields = "__all__"
    template_name = "exalted/characters/solars/solarcharm/create.html"


class SolarCharmUpdateView(UpdateView):
    model = SolarCharm
    fields = "__all__"
    template_name = "exalted/characters/solars/solarcharm/update.html"
