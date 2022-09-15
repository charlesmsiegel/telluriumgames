from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from exalted.forms import ExaltedAbilitiesForm, ExaltedAttributeForm, SolarCreationForm
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
                char.archery = form.data["archery"]
                char.athletics = form.data["athletics"]
                char.awareness = form.data["awareness"]
                char.brawl = form.data["brawl"]
                char.bureaucracy = form.data["bureaucracy"]
                char.craft = form.data["craft"]
                char.dodge = form.data["dodge"]
                char.integrity = form.data["integrity"]
                char.investigation = form.data["investigation"]
                char.larceny = form.data["larceny"]
                char.linguistics = form.data["linguistics"]
                char.lore = form.data["lore"]
                char.martial_arts = form.data["martial_arts"]
                if form.data["martial_arts"] > 0:
                    char.add_merit(ExMerit.objects.get(name="Martial Artist"))
                char.medicine = form.data["medicine"]
                char.melee = form.data["melee"]
                char.occult = form.data["occult"]
                char.performance = form.data["performance"]
                char.presence = form.data["presence"]
                char.resistance = form.data["resistance"]
                char.ride = form.data["ride"]
                char.sail = form.data["sail"]
                char.socialize = form.data["socialize"]
                char.stealth = form.data["stealth"]
                char.survival = form.data["survival"]
                char.thrown = form.data["thrown"]
                char.war = form.data["war"]
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
