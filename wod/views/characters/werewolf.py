from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, View

from wod.models.characters.human import MeritFlawRating
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


class WerewolfDetailView(View):
    def get(self, request, *args, **kwargs):
        werewolf = Werewolf.objects.get(pk=kwargs["pk"])
        context = self.get_context(werewolf)
        return render(request, "wod/characters/werewolf/werewolf/detail.html", context)

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


class WerewolfCreateView(CreateView):
    model = Werewolf
    fields = "__all__"
    template_name = "wod/characters/werewolf/werewolf/form.html"


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
        context['allowed'] = []
        for key, value in gift.allowed.items():
            value = sorted(value)
            context['allowed'].append(f"{key.title()}: {', '.join([x.title() for x in value])}")
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
