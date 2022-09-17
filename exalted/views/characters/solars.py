from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from exalted.forms import (
    ExaltedAbilitiesForm,
    ExaltedAttributeForm,
    SolarCreationForm,
    ExaltedMeritsForm,
)
from exalted.models.characters.mortals import ExSpecialty, MeritRating, ExMerit
from exalted.models.characters.solars import Solar, SolarCharm
from exalted.models.characters.utils import ABILITIES


class SolarDetailView(View):
    def get(self, request, *args, **kwargs):
        char = Solar.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)
        if char.status != "Un":
            return render(
                request, "exalted/characters/solars/solar/detail.html", context,
            )
        if char.creation_status == 1:
            context["form"] = ExaltedAttributeForm(initial=char.get_attributes())
            return render(
                request,
                "exalted/characters/solars/solar/creation_attribute.html",
                context,
            )
        if char.creation_status == 2:
            d = char.get_abilities()
            context["form"] = ExaltedAbilitiesForm(initial=d, character=char)
            return render(
                request,
                "exalted/characters/solars/solar/creation_abilities.html",
                context,
            )
        if char.creation_status == 3:
            context["form"] = ExaltedMeritsForm()
            return render(
                request,
                "exalted/characters/solars/solar/creation_merits.html",
                context,
            )
        if char.creation_status == 4:
            return render(
                request,
                "exalted/characters/solars/solar/creation_charms.html",
                context,
            )
        if char.creation_status == 5:
            return render(
                request,
                "exalted/characters/solars/solar/creation_intimacies.html",
                context,
            )
        if char.creation_status == 6:
            return render(
                request,
                "exalted/characters/solars/solar/creation_bonus_points.html",
                context,
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
                d = char.get_abilities()
                context["form"] = ExaltedAbilitiesForm(initial=d, character=char)
                return render(
                    request,
                    "exalted/characters/solars/solar/creation_abilities.html",
                    context,
                )
            context["form"] = ExaltedAttributeForm(initial=char.get_attributes())
            return render(
                request,
                "exalted/characters/solars/solar/creation_attribute.html",
                context,
            )
        if char.creation_status == 2:
            form = ExaltedAbilitiesForm(request.POST, character=char)
            if form.has_abilities(char):
                checked_abilities = [x for x in ABILITIES if x + "_check" in form.data]
                char.caste_abilities = [
                    x
                    for x in checked_abilities
                    if x in char.caste_ability_dict[char.caste]
                ]
                char.favored_abilities = [
                    x
                    for x in checked_abilities
                    if x not in char.caste_ability_dict[char.caste]
                ]
                form.full_clean()
                char.archery = form.cleaned_data["archery"]
                char.athletics = form.cleaned_data["athletics"]
                char.awareness = form.cleaned_data["awareness"]
                char.brawl = form.cleaned_data["brawl"]
                char.bureaucracy = form.cleaned_data["bureaucracy"]
                char.craft = form.cleaned_data["craft"]
                char.dodge = form.cleaned_data["dodge"]
                char.integrity = form.cleaned_data["integrity"]
                char.investigation = form.cleaned_data["investigation"]
                char.larceny = form.cleaned_data["larceny"]
                char.linguistics = form.cleaned_data["linguistics"]
                char.lore = form.cleaned_data["lore"]
                char.martial_arts = form.cleaned_data["martial_arts"]
                if form.cleaned_data["martial_arts"] > 0:
                    char.add_merit(ExMerit.objects.get(name="Martial Artist"))
                char.medicine = form.cleaned_data["medicine"]
                char.melee = form.cleaned_data["melee"]
                char.occult = form.cleaned_data["occult"]
                char.performance = form.cleaned_data["performance"]
                char.presence = form.cleaned_data["presence"]
                char.resistance = form.cleaned_data["resistance"]
                char.ride = form.cleaned_data["ride"]
                char.sail = form.cleaned_data["sail"]
                char.socialize = form.cleaned_data["socialize"]
                char.stealth = form.cleaned_data["stealth"]
                char.survival = form.cleaned_data["survival"]
                char.thrown = form.cleaned_data["thrown"]
                char.war = form.cleaned_data["war"]
                char.supernal_ability = form.data["supernal_ability"]

                s1 = ExSpecialty.objects.get_or_create(
                    ability=form.data["spec_1_ability"], name=form.data["spec_1_value"]
                )[0]
                s2 = ExSpecialty.objects.get_or_create(
                    ability=form.data["spec_2_ability"], name=form.data["spec_2_value"]
                )[0]
                s3 = ExSpecialty.objects.get_or_create(
                    ability=form.data["spec_3_ability"], name=form.data["spec_3_value"]
                )[0]
                s4 = ExSpecialty.objects.get_or_create(
                    ability=form.data["spec_4_ability"], name=form.data["spec_4_value"]
                )[0]

                char.add_specialty(s1)
                char.add_specialty(s2)
                char.add_specialty(s3)
                char.add_specialty(s4)

                char.creation_status += 1
                char.save()
                return render(
                    request,
                    "exalted/characters/solars/solar/creation_merits.html",
                    context,
                )
            d = char.get_abilities()
            context["form"] = ExaltedAbilitiesForm(initial=d, character=char)
            return render(
                request,
                "exalted/characters/solars/solar/creation_abilities.html",
                context,
            )
        if char.creation_status == 3:
            form = ExaltedMeritsForm(request.POST)
            if form.has_merits(char):
                form.full_clean()
                merits = [form.cleaned_data[f"merit_{i}"] for i in range(1, 11)]
                merit_ratings = [form.cleaned_data[f"merit_{i}_rating"] for i in range(1, 11)]
                pairs = list(zip(merits, merit_ratings))
                pairs = [x for x in pairs if x[0] != "----"]
                pairs = [(ExMerit.objects.get(name=x[0]), x[1]) for x in pairs]
                pairs = [(x[0], x[1]) for x in pairs if x[1] in x[0].ratings]
                for merit, rating in pairs:
                    MeritRating.objects.create(character=char, merit=merit, rating=rating)
                char.creation_status += 1
                char.save()
                return render(
                    request,
                    "exalted/characters/solars/solar/creation_charms.html",
                    context,
                )
            d = char.get_abilities()
            context["form"] = ExaltedMeritsForm()
            return render(
                request,
                "exalted/characters/solars/solar/creation_merits.html",
                context,
            )

    def get_context(self, char):
        return {
            "object": char,
            "merits": MeritRating.objects.filter(character=char).order_by(
                "merit__name"
            ),
            "specialties": char.specialties.all().order_by("name"),
        }


def load_merit_1_ratings(request):
    merit_name = request.GET.get("merit_1")
    ratings = ExMerit.objects.get(name=merit_name).ratings

    return render(
        request,
        "exalted/characters/solars/solar/load_rating_dropdown_list.html",
        {"ratings": ratings},
    )


def load_merit_2_ratings(request):
    merit_name = request.GET.get("merit_2")
    ratings = ExMerit.objects.get(name=merit_name).ratings

    return render(
        request,
        "exalted/characters/solars/solar/load_rating_dropdown_list.html",
        {"ratings": ratings},
    )


def load_merit_3_ratings(request):
    merit_name = request.GET.get("merit_3")
    ratings = ExMerit.objects.get(name=merit_name).ratings

    return render(
        request,
        "exalted/characters/solars/solar/load_rating_dropdown_list.html",
        {"ratings": ratings},
    )


def load_merit_4_ratings(request):
    merit_name = request.GET.get("merit_4")
    ratings = ExMerit.objects.get(name=merit_name).ratings

    return render(
        request,
        "exalted/characters/solars/solar/load_rating_dropdown_list.html",
        {"ratings": ratings},
    )


def load_merit_5_ratings(request):
    merit_name = request.GET.get("merit_5")
    ratings = ExMerit.objects.get(name=merit_name).ratings

    return render(
        request,
        "exalted/characters/solars/solar/load_rating_dropdown_list.html",
        {"ratings": ratings},
    )


def load_merit_6_ratings(request):
    merit_name = request.GET.get("merit_6")
    ratings = ExMerit.objects.get(name=merit_name).ratings

    return render(
        request,
        "exalted/characters/solars/solar/load_rating_dropdown_list.html",
        {"ratings": ratings},
    )


def load_merit_7_ratings(request):
    merit_name = request.GET.get("merit_7")
    ratings = ExMerit.objects.get(name=merit_name).ratings

    return render(
        request,
        "exalted/characters/solars/solar/load_rating_dropdown_list.html",
        {"ratings": ratings},
    )


def load_merit_8_ratings(request):
    merit_name = request.GET.get("merit_8")
    ratings = ExMerit.objects.get(name=merit_name).ratings

    return render(
        request,
        "exalted/characters/solars/solar/load_rating_dropdown_list.html",
        {"ratings": ratings},
    )


def load_merit_9_ratings(request):
    merit_name = request.GET.get("merit_9")
    ratings = ExMerit.objects.get(name=merit_name).ratings

    return render(
        request,
        "exalted/characters/solars/solar/load_rating_dropdown_list.html",
        {"ratings": ratings},
    )


def load_merit_10_ratings(request):
    merit_name = request.GET.get("merit_10")
    ratings = ExMerit.objects.get(name=merit_name).ratings

    return render(
        request,
        "exalted/characters/solars/solar/load_rating_dropdown_list.html",
        {"ratings": ratings},
    )


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
