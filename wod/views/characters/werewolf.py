from django.forms import formset_factory
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from core.views import BaseCharacterView
from game.models.chronicle import Chronicle
from wod.forms.characters.human import AttributeForm, MeritFlawForm
from wod.forms.characters.werewolf import (
    WerewolfAbilitiesForm,
    WerewolfAdvantagesForm,
    WerewolfCreationForm,
    WerewolfDescriptionForm,
    WerewolfFreebieForm,
    WerewolfPowersForm,
)
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
from wod.views.characters.human import AttributeDetailView


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
            )
            s.set_breed(form.data["breed"])
            s.set_auspice(form.data["auspice"])
            s.set_tribe(form.cleaned_data["tribe"])
            return redirect(s.get_absolute_url())
        context = {}
        context["form"] = WerewolfCreationForm()
        return render(request, "wod/characters/werewolf/werewolf/create.html", context)


class WerewolfAbilitiesDetailView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        werewolf = Werewolf.objects.get(pk=kwargs["pk"])
        context = self.get_context(werewolf)
        context["form"] = WerewolfAbilitiesForm(character=werewolf)
        return render(
            request, "wod/characters/werewolf/werewolf/2_abilities.html", context
        )

    def post(self, request, *args, **kwargs):
        werewolf = Werewolf.objects.get(pk=kwargs["pk"])
        context = self.get_context(werewolf)
        form = WerewolfAbilitiesForm(request.POST, character=werewolf)
        if "Back" in form.data:
            werewolf.prev_stage()
            return redirect(werewolf.get_absolute_url())
        if "Random Abilities" in form.data:
            werewolf.random_abilities()
            werewolf.next_stage()
            return redirect(werewolf.get_absolute_url())
        form.assign()
        if werewolf.has_abilities():
            werewolf.next_stage()
            return redirect(werewolf.get_absolute_url())
        context["form"] = WerewolfAbilitiesForm(character=werewolf)
        return redirect(werewolf.get_absolute_url())


class WerewolfAdvantagesView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        werewolf = Werewolf.objects.get(pk=kwargs["pk"])
        context = self.get_context(werewolf)

        context["form"] = WerewolfAdvantagesForm(character=werewolf)
        return render(
            request, "wod/characters/werewolf/werewolf/3_advantages.html", context,
        )

    def post(self, request, *args, **kwargs):
        character = Werewolf.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        form = WerewolfAdvantagesForm(request.POST, character=character)
        if "Back" in form.data:
            character.prev_stage()
            context["form"] = WerewolfAbilitiesForm(character=character)
            return redirect(character.get_absolute_url())
        if "Random Advantages" in form.data:
            character.random_backgrounds()
            character.next_stage()
            context["form"] = WerewolfPowersForm(character=character)
            return redirect(character.get_absolute_url())
        form.assign()
        if character.has_backgrounds():
            character.next_stage()
            context["form"] = WerewolfPowersForm(character=character)
            return redirect(character.get_absolute_url())
        context["form"] = WerewolfAdvantagesForm(character=character)
        return redirect(character.get_absolute_url())


class WerewolfPowersView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        werewolf = Werewolf.objects.get(pk=kwargs["pk"])
        context = self.get_context(werewolf)
        context["form"] = WerewolfPowersForm(character=werewolf)
        return render(
            request, "wod/characters/werewolf/werewolf/4_powers.html", context,
        )

    def post(self, request, *args, **kwargs):
        character = Werewolf.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        form = WerewolfPowersForm(request.POST, character=character)
        if "Back" in form.data:
            character.prev_stage()
            context["form"] = WerewolfAdvantagesForm(character=character)
            return redirect(character.get_absolute_url())
        if "Random Powers" in form.data:
            character.random_gifts()
            character.next_stage()
            MFFormset = formset_factory(MeritFlawForm, extra=1)
            context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
            context["form"] = WerewolfFreebieForm(character=character)
            return redirect(character.get_absolute_url())
        form.assign()
        if character.has_gifts() and character.total_resonance() > 0:
            character.next_stage()
            MFFormset = formset_factory(MeritFlawForm, extra=1)
            context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
            context["form"] = WerewolfFreebieForm(character=character)
            return redirect(character.get_absolute_url())
        context["form"] = WerewolfPowersForm(character=character)
        return redirect(character.get_absolute_url())


class WerewolfFreebiesView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        werewolf = Werewolf.objects.get(pk=kwargs["pk"])
        context = self.get_context(werewolf)
        MFFormset = formset_factory(MeritFlawForm, extra=1)
        context["formset"] = MFFormset(form_kwargs={"chartype": "garou"})
        context["form"] = WerewolfFreebieForm(character=werewolf)
        return render(
            request, "wod/characters/werewolf/werewolf/5_freebies.html", context,
        )

    def post(self, request, *args, **kwargs):
        character = Werewolf.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        form = WerewolfFreebieForm(request.POST, character=character)
        if "Back" in form.data:
            character.prev_stage()
            context["form"] = WerewolfPowersForm(character=character)
            return redirect(character.get_absolute_url())
        if "Random Freebies" in form.data:
            character.random_freebies()
            character.next_stage()
            context["form"] = WerewolfDescriptionForm(character=character)
            return redirect(character.get_absolute_url())
        form.full_clean()
        if form.total_cost_freebies() == character.freebies:
            form.assign()
            character.next_stage()
            context["form"] = WerewolfDescriptionForm(character=character)
            return redirect(character.get_absolute_url())
        MFFormset = formset_factory(MeritFlawForm, extra=1)
        context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
        context["form"] = WerewolfFreebieForm(character=character)
        return redirect(character.get_absolute_url())


class WerewolfDescriptionView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        werewolf = Werewolf.objects.get(pk=kwargs["pk"])
        context = self.get_context(werewolf)
        context["form"] = WerewolfDescriptionForm(character=werewolf)
        return render(
            request, "wod/characters/werewolf/werewolf/6_description.html", context,
        )

    def post(self, request, *args, **kwargs):
        character = Werewolf.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        form = WerewolfDescriptionForm(request.POST, character=character)
        if "Back" in form.data:
            character.prev_stage()
            MFFormset = formset_factory(MeritFlawForm, extra=1)
            context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
            context["form"] = WerewolfFreebieForm(character=character)
            return redirect(character.get_absolute_url())
        if "Random Description" in form.data:
            character.update_status("Sub")
            character.random_history()
            character.random_werewolf_history()
            character.random_finishing_touches()
            character.mf_based_corrections()
            character.next_stage()
            return redirect(character.get_absolute_url())
        form.full_clean()
        if form.complete():
            for key, value in form.cleaned_data.items():
                setattr(character, key, value)
            character.next_stage()
            return redirect(character.get_absolute_url())
        context["form"] = WerewolfDescriptionForm(character=character)
        return redirect(character.get_absolute_url())


class WerewolfDetailView(BaseCharacterView):
    stage_views = {
        1: AttributeDetailView,
        2: WerewolfAbilitiesDetailView,
        3: WerewolfAdvantagesView,
        4: WerewolfPowersView,
        5: WerewolfFreebiesView,
        6: WerewolfDescriptionView,
    }

    def get(self, request, *args, **kwargs):
        char = Werewolf.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)
        if char.status != "Un":
            return render(
                request, "wod/characters/werewolf/werewolf/detail.html", context
            )
        if char.creation_status in self.stage_views.keys():
            return self.stage_views[char.creation_status].as_view()(
                request, *args, **kwargs
            )
        return render(request, "wod/characters/werewolf/werewolf/detail.html", context)

    def post(self, request, *args, **kwargs):
        char = Werewolf.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)
        if char.creation_status in self.stage_views.keys():
            return self.stage_views[char.creation_status].as_view()(
                request, *args, **kwargs
            )
        return render(request, "wod/characters/werewolf/werewolf/detail.html", context)

    def get_context(self, character):
        context = super().get_context(character)
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
        context["rank_name"] = character.rank_names[character.rank]
        return context


class WerewolfUpdateView(UpdateView):
    model = Werewolf
    fields = "__all__"
    template_name = "wod/characters/werewolf/werewolf/form.html"


class KinfolkDetailView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        kinfolk = Kinfolk.objects.get(pk=kwargs["pk"])
        context = self.get_context(kinfolk)
        return render(request, "wod/characters/werewolf/kinfolk/detail.html", context)

    def get_context(self, kinfolk):
        context = super().get_context(kinfolk)
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
