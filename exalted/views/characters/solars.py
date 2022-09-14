from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from exalted.forms import ExaltedAttributeForm, SolarCreationForm
from exalted.models.characters.mortals import MeritRating
from exalted.models.characters.solars import Solar, SolarCharm


class SolarDetailView(View):
    def get(self, request, *args, **kwargs):
        char = Solar.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)
        if char.status != "Un":
            return render(
                request, "exalted/characters/solars/solar/detail.html", context,
            )
        if char.creation_status == 1:
            print("Status 1: Attributes")
            context["form"] = ExaltedAttributeForm(
                initial={
                    "strength": char.strength,
                    "charisma": char.charisma,
                    "perception": char.perception,
                    "dexterity": char.dexterity,
                    "manipulation": char.manipulation,
                    "intelligence": char.intelligence,
                    "stamina": char.stamina,
                    "appearance": char.appearance,
                    "wits": char.wits,
                }
            )
            return render(
                request,
                "exalted/characters/solars/solar/creation_attribute.html",
                context,
            )
        if char.creation_status == 2:
            return render(
                request, "exalted/characters/solars/solar/detail.html", context,
            )
        if char.creation_status == 3:
            print("Status 3: Merits")
            return render(
                request, "exalted/characters/solars/solar/detail.html", context,
            )
        if char.creation_status == 4:
            print("Status 4: Charms")
            return render(
                request, "exalted/characters/solars/solar/detail.html", context,
            )
        if char.creation_status == 5:
            print("Status 5: Limit Trigger and Intimacies")
            return render(
                request, "exalted/characters/solars/solar/detail.html", context,
            )
        if char.creation_status == 6:
            print("Status 6: Bonus Points")
            return render(
                request, "exalted/characters/solars/solar/detail.html", context,
            )
        return render(request, "exalted/characters/solars/solar/detail.html", context,)

    def post(self, request, *args, **kwargs):
        char = Solar.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)
        if char.creation_status == 1:
            form = ExaltedAttributeForm(request.POST)
            if form.has_attributes():
                char.strength = form.data["strength"]
                char.dexterity = form.data["dexterity"]
                char.stamina = form.data["stamina"]
                char.charisma = form.data["charisma"]
                char.manipulation = form.data["manipulation"]
                char.appearance = form.data["appearance"]
                char.perception = form.data["perception"]
                char.intelligence = form.data["intelligence"]
                char.wits = form.data["wits"]
                char.creation_status += 1
                char.save()
                return render(
                    request, "exalted/characters/solars/solar/detail.html", context,
                )
            return render(
                request, "exalted/characters/solars/solar/detail.html", context,
            )

    def get_context(self, char):
        return {
            "object": char,
            "merits": MeritRating.objects.filter(character=char).order_by(
                "merit__name"
            ),
            "specialties": char.specialties.all().order_by("name"),
        }


class SolarCreateView(View):
    def get(self, request, *args, **kwargs):
        context = dict()
        context["form"] = SolarCreationForm()
        return render(request, "exalted/characters/solars/solar/create.html", context)

    def post(self, request, *args, **kwargs):
        form = SolarCreationForm(request.POST)
        s = Solar.objects.create(
            name=form.data["name"],
            concept=form.data["concept"],
            caste=form.data["caste"],
            owner=request.user,
            status="Un",
        )
        return redirect(s.get_absolute_url())


# class SolarCreateView(CreateView):
#     model = Solar
#     fields = "__all__"
#     template_name = "exalted/characters/solars/solar/form.html"


class SolarUpdateView(UpdateView):
    model = Solar
    fields = "__all__"
    template_name = "exalted/characters/solars/solar/form.html"


class SolarCharmDetailView(DetailView):
    model = SolarCharm
    template_name = "exalted/characters/solars/solarcharm/detail.html"


class SolarCharmCreateView(CreateView):
    model = SolarCharm
    fields = "__all__"
    template_name = "exalted/characters/solars/solarcharm/form.html"


class SolarCharmUpdateView(UpdateView):
    model = SolarCharm
    fields = "__all__"
    template_name = "exalted/characters/solars/solarcharm/form.html"
