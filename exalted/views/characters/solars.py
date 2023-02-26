from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from exalted.forms import (
    ExaltedAbilitiesForm,
    ExaltedAttributeForm,
    ExaltedCharmForm,
    ExaltedIntimacyForm,
    ExaltedMeritsForm,
    SolarCreationForm,
)
from exalted.models.characters.charms import (
    Charm,
    MartialArtsCharm,
    MartialArtsStyle,
    SolarCharm,
)
from exalted.models.characters.mortals import (
    ExMerit,
    ExSpecialty,
    Intimacy,
    MeritRating,
)
from exalted.models.characters.solars import Solar
from exalted.models.characters.utils import ABILITIES
from game.models import Chronicle


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
            context["form"] = ExaltedCharmForm(character=char)
            return render(
                request,
                "exalted/characters/solars/solar/creation_charms.html",
                context,
            )
        if char.creation_status == 5:
            context["form"] = ExaltedIntimacyForm()
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
                context["form"] = ExaltedMeritsForm()
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
                merit_ratings = [
                    form.cleaned_data[f"merit_{i}_rating"] for i in range(1, 11)
                ]
                pairs = list(zip(merits, merit_ratings))
                pairs = [x for x in pairs if x[0] != "----"]
                pairs = [(ExMerit.objects.get(name=x[0]), x[1]) for x in pairs]
                pairs = [(x[0], x[1]) for x in pairs if x[1] in x[0].ratings]
                for merit, rating in pairs:
                    MeritRating.objects.create(
                        character=char, merit=merit, rating=rating
                    )
                char.creation_status += 1
                char.save()
                context["form"] = ExaltedCharmForm(character=char)
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
        if char.creation_status == 4:
            form = ExaltedCharmForm(request.POST, character=char)
            form.full_clean()
            charm_name = form.cleaned_data["charm"]
            c = Charm.objects.get(name=charm_name)
            char.add_charm(c)
            if char.has_charms():
                char.creation_status += 1
                char.save()
                context["form"] = ExaltedIntimacyForm()
                return render(
                    request,
                    "exalted/characters/solars/solar/creation_intimacies.html",
                    context,
                )
            context["form"] = ExaltedCharmForm(character=char)
            return render(
                request,
                "exalted/characters/solars/solar/creation_charms.html",
                context,
            )
        if char.creation_status == 5:
            form = ExaltedIntimacyForm(request.POST)
            if form.has_intimacies():
                form.full_clean()
                i1 = Intimacy.objects.create(
                    name=form.cleaned_data["intimacy_1"],
                    intimacy_type=form.cleaned_data["intimacy_type_1"],
                    strength=form.cleaned_data["intimacy_strength_1"],
                    is_negative=form.cleaned_data["is_negative_1"],
                )
                i2 = Intimacy.objects.create(
                    name=form.cleaned_data["intimacy_2"],
                    intimacy_type=form.cleaned_data["intimacy_type_2"],
                    strength=form.cleaned_data["intimacy_strength_2"],
                    is_negative=form.cleaned_data["is_negative_2"],
                )
                i3 = Intimacy.objects.create(
                    name=form.cleaned_data["intimacy_3"],
                    intimacy_type=form.cleaned_data["intimacy_type_3"],
                    strength=form.cleaned_data["intimacy_strength_3"],
                    is_negative=form.cleaned_data["is_negative_3"],
                )
                i4 = Intimacy.objects.create(
                    name=form.cleaned_data["intimacy_4"],
                    intimacy_type=form.cleaned_data["intimacy_type_4"],
                    strength=form.cleaned_data["intimacy_strength_4"],
                    is_negative=form.cleaned_data["is_negative_4"],
                )
                char.add_intimacy(i1)
                char.add_intimacy(i2)
                char.add_intimacy(i3)
                char.add_intimacy(i4)
                char.limit_trigger = form.cleaned_data["limit_trigger"]
                char.creation_status += 1
                char.save()
                char.apply_finishing_touches()
                return render(
                    request,
                    "exalted/characters/solars/solar/creation_bonus_points.html",
                    context,
                )
            context["form"] = ExaltedIntimacyForm()
            return render(
                request,
                "exalted/characters/solars/solar/creation_intimacies.html",
                context,
            )
        if char.creation_status == 6:
            pass

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
        context = {}
        context["form"] = SolarCreationForm()
        return render(request, "exalted/characters/solars/solar/create.html", context)

    def post(self, request, *args, **kwargs):
        form = SolarCreationForm(request.POST)
        chron = None
        if "chronicle" in form.data.keys():
            chron = Chronicle.objects.filter(name=form.data["chronicle"]).first()
        s = Solar.objects.create(
            name=form.data["name"],
            concept=form.data["concept"],
            caste=form.data["caste"],
            anima=form.data["anima"],
            owner=request.user,
            status="Un",
            essence=1,
            chronicle=chron,
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
