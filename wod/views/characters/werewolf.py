from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from game.models.chronicle import Chronicle
from wod.forms.characters.human import AttributeForm
from wod.forms.characters.werewolf import WerewolfAbilitiesForm, WerewolfCreationForm
from wod.models.characters.human import Archetype, MeritFlawRating
from wod.models.characters.werewolf.fomori import Fomor, FomoriPower
from wod.models.characters.werewolf.garou import (
    BattleScar,
    Camp,
    Gift,
    Pack,
    RenownIncident,
    Rite,
    Tribe,
    Werewolf,
)
from wod.models.characters.werewolf.kinfolk import Kinfolk
from wod.models.characters.werewolf.spirits import SpiritCharacter, SpiritCharm, Totem


class WerewolfCreateView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context["form"] = WerewolfCreationForm()
        return render(request, "wod/characters/werewolf/werewolf/create.html", context)

    def post(self, request, *args, **kwargs):
        if "Full Random" in request.POST:
            s = Werewolf.objects.create(owner=request.user, status="Un")
            s.random()
            return redirect(s.get_absolute_url())
        if "Random Basics" in request.POST:
            s = Werewolf.objects.create(owner=request.user, status="Un", rank=1)
            s.random_name()
            s.random_concept()
            s.random_archetypes()
            s.random_tribe()
            s.random_auspice()
            s.random_breed()
            s.save()
            return redirect(s.get_absolute_url())
        if "Save" in request.POST:
            form = WerewolfCreationForm(request.POST)
            form.full_clean()
            s = Werewolf.objects.create(
                name=form.data["name"],
                concept=form.data["concept"],
                demeanor=form.cleaned_data["demeanor"],
                nature=form.cleaned_data["nature"],
                owner=request.user,
                status="Un",
                chronicle=form.cleaned_data["chronicle"],
                rank=1,
                tribe=form.cleaned_data["tribe"],
                auspice=form.data["auspice"],
                breed=form.data["breed"],
            )
            return redirect(s.get_absolute_url())
        context = {}
        context["form"] = WerewolfCreationForm()
        return render(request, "wod/characters/werewolf/werewolf/create.html", context)


class WerewolfDetailView(View):
    def get(self, request, *args, **kwargs):
        werewolf = Werewolf.objects.get(pk=kwargs["pk"])
        context = self.get_context(werewolf)
        if werewolf.status != "Un":
            return render(request, "wod/characters/werewolf/werewolf/detail.html", context)
        if werewolf.creation_status == 1:
            context["form"] = AttributeForm(character=werewolf)
            return render(
                request, "wod/characters/werewolf/werewolf/1_attribute.html", context,
            )
        if werewolf.creation_status == 2:
            context["form"] = WerewolfAbilitiesForm(character=werewolf)
            return render(
                request, "wod/characters/werewolf/werewolf/2_abilities.html", context,
            )
        if werewolf.creation_status == 3:
            # context["form"] = MageAdvantagesForm(character=werewolf)
            return render(
                request, "wod/characters/werewolf/werewolf/3_advantages.html", context,
            )
        if werewolf.creation_status == 4:
            # context["form"] = MagePowersForm(character=werewolf)
            return render(request, "wod/characters/werewolf/werewolf/4_powers.html", context,)
        if werewolf.creation_status == 5:
            # MFFormset = formset_factory(MageMeritFlawForm, extra=1)
            # context["formset"] = MFFormset()
            # context["form"] = MageFreebieForm(character=werewolf)
            return render(request, "wod/characters/werewolf/werewolf/5_freebies.html", context,)
        if werewolf.creation_status == 6:
            # context["form"] = MageDescriptionForm(character=werewolf)
            return render(
                request, "wod/characters/werewolf/werewolf/6_description.html", context,
            )
        return render(request, "wod/characters/werewolf/werewolf/detail.html", context)

    def post(self, request, *args, **kwargs):
        char = Werewolf.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)
        if char.creation_status == 1:
            form = AttributeForm(request.POST, character=char)
            if "Random Attributes" in form.data:
                char.random_attributes()
                char.next_stage()
                context["form"] = WerewolfAbilitiesForm(character=char)
                return render(
                    request, "wod/characters/werewolf/werewolf/2_abilities.html", context,
                )
            form.assign()
            if char.has_attributes():
                char.next_stage()
                context["form"] = WerewolfAbilitiesForm(character=char)
                return render(
                    request, "wod/characters/werewolf/werewolf/2_abilities.html", context,
                )
            context["form"] = AttributeForm(character=char)
            return render(
                request, "wod/characters/werewolf/werewolf/1_attribute.html", context,
            )
        if char.creation_status == 2:
            form = WerewolfAbilitiesForm(request.POST, character=char)
            if "Back" in form.data:
                char.prev_stage()
                context["form"] = AttributeForm(character=char)
                return render(
                    request, "wod/characters/werewolf/werewolf/1_attribute.html", context,
                )
            if "Random Abilities" in form.data:
                char.random_abilities()
                char.next_stage()
                # context["form"] = MageAdvantagesForm(character=char)
                return render(
                    request, "wod/characters/werewolf/werewolf/3_advantages.html", context,
                )
            form.assign()
            if char.has_abilities():
                char.next_stage()
                # context["form"] = MageAdvantagesForm(character=char)
                return render(
                    request, "wod/characters/werewolf/werewolf/3_advantages.html", context,
                )
            context["form"] = WerewolfAbilitiesForm(character=char)
            return render(
                request, "wod/characters/werewolf/werewolf/2_abilities.html", context,
            )
        if char.creation_status == 3:
            # form = MageAdvantagesForm(request.POST, character=char)
            if "Back" in form.data:
                char.prev_stage()
                context["form"] = WerewolfAbilitiesForm(character=char)
                return render(
                    request, "wod/characters/werewolf/werewolf/2_abilities.html", context,
                )
            if "Random Advantages" in form.data:
                char.random_focus()
                char.random_backgrounds()
                char.random_arete()
                char.random_affinity_sphere()
                char.next_stage()
                # context["resonances"] = Resonance.objects.all().order_by("name")
                # context["form"] = MagePowersForm(character=char)
                return render(
                    request, "wod/characters/werewolf/werewolf/4_powers.html", context,
                )
            form.assign()
            if (
                char.has_backgrounds()
                and char.has_affinity_sphere()
                and char.has_focus()
            ):
                char.next_stage()
                # context["resonances"] = Resonance.objects.all().order_by("name")
                # context["form"] = MagePowersForm(character=char)
                return render(
                    request, "wod/characters/werewolf/werewolf/4_powers.html", context,
                )
            # context["form"] = MageAdvantagesForm(character=char)
            return render(
                request, "wod/characters/werewolf/werewolf/3_advantages.html", context,
            )
        if char.creation_status == 4:
            # form = MagePowersForm(request.POST, character=char)
            if "Back" in form.data:
                char.prev_stage()
                # context["form"] = MageAdvantagesForm(character=char)
                return render(
                    request, "wod/characters/werewolf/werewolf/3_advantages.html", context,
                )
            if "Random Powers" in form.data:
                char.random_spheres()
                char.random_resonance()
                char.next_stage()
                # MFFormset = formset_factory(MageMeritFlawForm, extra=1)
                # context["formset"] = MFFormset()
                # context["form"] = MageFreebieForm(character=char)
                return render(
                    request, "wod/characters/werewolf/werewolf/5_freebies.html", context,
                )
            form.assign()
            if char.has_spheres() and char.total_resonance() > 0:
                char.next_stage()
                # MFFormset = formset_factory(MageMeritFlawForm, extra=1)
                # context["formset"] = MFFormset()
                # context["form"] = MageFreebieForm(character=char)
                return render(
                    request, "wod/characters/werewolf/werewolf/5_freebies.html", context,
                )
            # context["resonances"] = Resonance.objects.all().order_by("name")
            # context["form"] = MagePowersForm(character=char)
            return render(request, "wod/characters/werewolf/werewolf/4_powers.html", context,)
        if char.creation_status == 5:
            # form = MageFreebieForm(request.POST, character=char)
            if "Back" in form.data:
                char.prev_stage()
                # context["resonances"] = Resonance.objects.all().order_by("name")
                # context["form"] = MagePowersForm(character=char)
                return render(
                    request, "wod/characters/werewolf/werewolf/4_powers.html", context,
                )
            if "Random Freebies" in form.data:
                char.random_freebies()
                char.next_stage()
                # context["form"] = MageDescriptionForm(character=char)
                return render(
                    request, "wod/characters/werewolf/werewolf/6_description.html", context,
                )
            form.full_clean()
            if form.total_cost_freebies() == char.freebies:
                form.assign()
                char.next_stage()
                # context["form"] = MageDescriptionForm(character=char)
                return render(
                    request, "wod/characters/werewolf/werewolf/6_description.html", context,
                )
            # MFFormset = formset_factory(MageMeritFlawForm, extra=1)
            # context["formset"] = MFFormset()
            # context["form"] = MageFreebieForm(character=char)
            return render(request, "wod/characters/werewolf/werewolf/5_freebies.html", context,)
        if char.creation_status == 6:
            # form = MageDescriptionForm(request.POST, character=char)
            if "Back" in form.data:
                char.prev_stage()
                # MFFormset = formset_factory(MageMeritFlawForm, extra=1)
                # context["formset"] = MFFormset()
                # context["form"] = MageFreebieForm(character=char)
                return render(
                    request, "wod/characters/werewolf/werewolf/5_freebies.html", context,
                )
            if "Random Description" in form.data:
                char.update_status("Sub")
                char.random_history()
                char.random_mage_history()
                char.mf_based_corrections()
                char.next_stage()
                return render(request, "wod/characters/werewolf/werewolf/detail.html", context,)
            form.full_clean()
            if form.complete():
                for key, value in form.cleaned_data.items():
                    setattr(char, key, value)
                char.next_stage()
                return render(request, "wod/characters/werewolf/werewolf/detail.html", context,)
            # context["form"] = MageDescriptionForm(character=char)
            return render(
                request, "wod/characters/werewolf/werewolf/6_description.html", context,
            )
        return render(request, "wod/characters/werewolf/werewolf/detail.html", context,)

    def get_context(self, werewolf):
        context = {"object": werewolf}
        specialties = {}
        for attribute in werewolf.get_attributes():
            specialties[attribute] = ", ".join(
                [x.name for x in werewolf.specialties.filter(stat=attribute)]
            )
        for ability in werewolf.get_abilities():
            specialties[ability] = ", ".join(
                [x.name for x in werewolf.specialties.filter(stat=ability)]
            )
        for key, value in specialties.items():
            context[f"{key}_spec"] = value

        context["merits_and_flaws"] = MeritFlawRating.objects.order_by(
            "mf__name"
        ).filter(character=werewolf)
        all_gifts = list(context["object"].gifts.all())
        row_length = 3
        all_gifts = [
            all_gifts[i : i + row_length] for i in range(0, len(all_gifts), row_length)
        ]
        context["gifts"] = all_gifts

        all_rites = list(context["object"].rites_known.all())
        row_length = 3
        all_rites = [
            all_rites[i : i + row_length] for i in range(0, len(all_rites), row_length)
        ]
        context["rites"] = all_rites
        context["rank_name"] = werewolf.rank_names[werewolf.rank]
        return context


class WerewolfUpdateView(UpdateView):
    model = Werewolf
    fields = "__all__"
    template_name = "wod/characters/werewolf/werewolf/form.html"


class KinfolkDetailView(View):
    def get(self, request, *args, **kwargs):
        kinfolk = Kinfolk.objects.get(pk=kwargs["pk"])
        context = self.get_context(kinfolk)
        return render(request, "wod/characters/werewolf/kinfolk/detail.html", context)

    def get_context(self, kinfolk):
        context = {"object": kinfolk}
        specialties = {}
        for attribute in kinfolk.get_attributes():
            specialties[attribute] = ", ".join(
                [x.name for x in kinfolk.specialties.filter(stat=attribute)]
            )
        for ability in kinfolk.get_abilities():
            specialties[ability] = ", ".join(
                [x.name for x in kinfolk.specialties.filter(stat=ability)]
            )
        for key, value in specialties.items():
            context[f"{key}_spec"] = value

        context["merits_and_flaws"] = MeritFlawRating.objects.order_by(
            "mf__name"
        ).filter(character=kinfolk)
        all_gifts = list(context["object"].gifts.all())
        row_length = 3
        all_gifts = [
            all_gifts[i : i + row_length] for i in range(0, len(all_gifts), row_length)
        ]
        context["gifts"] = all_gifts

        return context


class KinfolkCreateView(CreateView):
    model = Kinfolk
    fields = "__all__"
    template_name = "wod/characters/werewolf/kinfolk/form.html"


class KinfolkUpdateView(UpdateView):
    model = Kinfolk
    fields = "__all__"
    template_name = "wod/characters/werewolf/kinfolk/form.html"


class SpiritDetailView(DetailView):
    model = SpiritCharacter
    template_name = "wod/characters/werewolf/spirit/detail.html"


class SpiritCreateView(CreateView):
    model = SpiritCharacter
    fields = "__all__"
    template_name = "wod/characters/werewolf/spirit/form.html"


class SpiritUpdateView(UpdateView):
    model = SpiritCharacter
    fields = "__all__"
    template_name = "wod/characters/werewolf/spirit/form.html"


class PackDetailView(DetailView):
    model = Pack
    template_name = "wod/characters/werewolf/pack/detail.html"


class PackCreateView(CreateView):
    model = Pack
    fields = "__all__"
    template_name = "wod/characters/werewolf/pack/form.html"


class PackUpdateView(UpdateView):
    model = Pack
    fields = "__all__"
    template_name = "wod/characters/werewolf/pack/form.html"


class CampDetailView(DetailView):
    model = Camp
    template_name = "wod/characters/werewolf/camp/detail.html"


class CampCreateView(CreateView):
    model = Camp
    fields = "__all__"
    template_name = "wod/characters/werewolf/camp/form.html"


class CampUpdateView(UpdateView):
    model = Camp
    fields = "__all__"
    template_name = "wod/characters/werewolf/camp/form.html"


class GiftDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        gift = Gift.objects.get(pk=kwargs["pk"])
        context = self.get_context(gift)
        return render(request, "wod/characters/werewolf/gift/detail.html", context)

    def get_context(self, gift):
        context = {}
        context["object"] = gift
        context["allowed"] = []
        for key, value in gift.allowed.items():
            value = sorted(value)
            context["allowed"].append(
                f"{key.title()}: {', '.join([x.title() for x in value])}"
            )
        return context


class GiftCreateView(CreateView):
    model = Gift
    fields = ["name", "rank", "allowed", "description"]
    template_name = "wod/characters/werewolf/gift/form.html"


class GiftUpdateView(UpdateView):
    model = Gift
    fields = ["name", "rank", "allowed", "description"]
    template_name = "wod/characters/werewolf/gift/form.html"


class RenownIncidentDetailView(DetailView):
    model = RenownIncident
    template_name = "wod/characters/werewolf/renownincident/detail.html"


class RenownIncidentCreateView(CreateView):
    model = RenownIncident
    fields = "__all__"
    template_name = "wod/characters/werewolf/renownincident/form.html"


class RenownIncidentUpdateView(UpdateView):
    model = RenownIncident
    fields = "__all__"
    template_name = "wod/characters/werewolf/renownincident/form.html"


class RiteDetailView(DetailView):
    model = Rite
    template_name = "wod/characters/werewolf/rite/detail.html"


class RiteCreateView(CreateView):
    model = Rite
    fields = ["name", "level", "rite_type", "description"]
    template_name = "wod/characters/werewolf/rite/form.html"


class RiteUpdateView(UpdateView):
    model = Rite
    fields = ["name", "level", "rite_type", "description"]
    template_name = "wod/characters/werewolf/rite/form.html"


class TotemDetailView(DetailView):
    model = Totem
    template_name = "wod/characters/werewolf/totem/detail.html"


class TotemCreateView(CreateView):
    model = Totem
    fields = "__all__"
    template_name = "wod/characters/werewolf/totem/form.html"


class TotemUpdateView(UpdateView):
    model = Totem
    fields = "__all__"
    template_name = "wod/characters/werewolf/totem/form.html"


class TribeDetailView(DetailView):
    model = Tribe
    template_name = "wod/characters/werewolf/tribe/detail.html"


class TribeCreateView(CreateView):
    model = Tribe
    fields = ["name", "willpower", "description"]
    template_name = "wod/characters/werewolf/tribe/form.html"


class TribeUpdateView(UpdateView):
    model = Tribe
    fields = ["name", "willpower", "description"]
    template_name = "wod/characters/werewolf/tribe/form.html"


class CharmDetailView(DetailView):
    model = SpiritCharm
    template_name = "wod/characters/werewolf/charm/detail.html"


class CharmCreateView(CreateView):
    model = SpiritCharm
    fields = "__all__"
    template_name = "wod/characters/werewolf/charm/form.html"


class CharmUpdateView(UpdateView):
    model = SpiritCharm
    fields = "__all__"
    template_name = "wod/characters/werewolf/charm/form.html"


class BattleScarDetailView(DetailView):
    model = BattleScar
    template_name = "wod/characters/werewolf/battlescar/detail.html"


class BattleScarCreateView(CreateView):
    model = BattleScar
    fields = "__all__"
    template_name = "wod/characters/werewolf/battlescar/form.html"


class BattleScarUpdateView(UpdateView):
    model = BattleScar
    fields = "__all__"
    template_name = "wod/characters/werewolf/battlescar/form.html"


class FomorDetailView(DetailView):
    model = Fomor
    template_name = "wod/characters/werewolf/fomor/detail.html"


class FomorCreateView(CreateView):
    model = Fomor
    fields = "__all__"
    template_name = "wod/characters/werewolf/fomor/form.html"


class FomorUpdateView(UpdateView):
    model = Fomor
    fields = "__all__"
    template_name = "wod/characters/werewolf/fomor/form.html"


class FomoriPowerDetailView(DetailView):
    model = FomoriPower
    template_name = "wod/characters/werewolf/fomoripower/detail.html"


class FomoriPowerCreateView(CreateView):
    model = FomoriPower
    fields = ["name", "description"]
    template_name = "wod/characters/werewolf/fomoripower/form.html"


class FomoriPowerUpdateView(UpdateView):
    model = FomoriPower
    fields = ["name", "description"]
    template_name = "wod/characters/werewolf/fomoripower/form.html"
