from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, View

from wod.models.characters.human import MeritFlawRating
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
    template_name = "wod/characters/werewolf/werewolf/create.html"


class WerewolfUpdateView(UpdateView):
    model = Werewolf
    fields = "__all__"
    template_name = "wod/characters/werewolf/werewolf/update.html"


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
    template_name = "wod/characters/werewolf/kinfolk/create.html"


class KinfolkUpdateView(UpdateView):
    model = Kinfolk
    fields = "__all__"
    template_name = "wod/characters/werewolf/kinfolk/update.html"


class SpiritDetailView(DetailView):
    model = SpiritCharacter
    template_name = "wod/characters/werewolf/spirit/detail.html"


class SpiritCreateView(CreateView):
    model = SpiritCharacter
    fields = "__all__"
    template_name = "wod/characters/werewolf/spirit/create.html"


class SpiritUpdateView(UpdateView):
    model = SpiritCharacter
    fields = "__all__"
    template_name = "wod/characters/werewolf/spirit/update.html"


class PackDetailView(DetailView):
    model = Pack
    template_name = "wod/characters/werewolf/pack/detail.html"


class PackCreateView(CreateView):
    model = Pack
    fields = "__all__"
    template_name = "wod/characters/werewolf/pack/create.html"


class PackUpdateView(UpdateView):
    model = Pack
    fields = "__all__"
    template_name = "wod/characters/werewolf/pack/update.html"


class CampDetailView(DetailView):
    model = Camp
    template_name = "wod/characters/werewolf/camp/detail.html"


class CampCreateView(CreateView):
    model = Camp
    fields = "__all__"
    template_name = "wod/characters/werewolf/camp/create.html"


class CampUpdateView(UpdateView):
    model = Camp
    fields = "__all__"
    template_name = "wod/characters/werewolf/camp/update.html"


class GiftDetailView(DetailView):
    model = Gift
    template_name = "wod/characters/werewolf/gift/detail.html"


class GiftCreateView(CreateView):
    model = Gift
    fields = "__all__"
    template_name = "wod/characters/werewolf/gift/create.html"


class GiftUpdateView(UpdateView):
    model = Gift
    fields = "__all__"
    template_name = "wod/characters/werewolf/gift/update.html"


class RenownIncidentDetailView(DetailView):
    model = RenownIncident
    template_name = "wod/characters/werewolf/renownincident/detail.html"


class RenownIncidentCreateView(CreateView):
    model = RenownIncident
    fields = "__all__"
    template_name = "wod/characters/werewolf/renownincident/create.html"


class RenownIncidentUpdateView(UpdateView):
    model = RenownIncident
    fields = "__all__"
    template_name = "wod/characters/werewolf/renownincident/update.html"


class RiteDetailView(DetailView):
    model = Rite
    template_name = "wod/characters/werewolf/rite/detail.html"


class RiteCreateView(CreateView):
    model = Rite
    fields = "__all__"
    template_name = "wod/characters/werewolf/rite/create.html"


class RiteUpdateView(UpdateView):
    model = Rite
    fields = "__all__"
    template_name = "wod/characters/werewolf/rite/update.html"


class TotemDetailView(DetailView):
    model = Totem
    template_name = "wod/characters/werewolf/totem/detail.html"


class TotemCreateView(CreateView):
    model = Totem
    fields = "__all__"
    template_name = "wod/characters/werewolf/totem/create.html"


class TotemUpdateView(UpdateView):
    model = Totem
    fields = "__all__"
    template_name = "wod/characters/werewolf/totem/update.html"


class TribeDetailView(DetailView):
    model = Tribe
    template_name = "wod/characters/werewolf/tribe/detail.html"


class TribeCreateView(CreateView):
    model = Tribe
    fields = "__all__"
    template_name = "wod/characters/werewolf/tribe/create.html"


class TribeUpdateView(UpdateView):
    model = Tribe
    fields = "__all__"
    template_name = "wod/characters/werewolf/tribe/update.html"


class CharmDetailView(DetailView):
    model = SpiritCharm
    template_name = "wod/characters/werewolf/charm/detail.html"


class CharmCreateView(CreateView):
    model = SpiritCharm
    fields = "__all__"
    template_name = "wod/characters/werewolf/charm/create.html"


class CharmUpdateView(UpdateView):
    model = SpiritCharm
    fields = "__all__"
    template_name = "wod/characters/werewolf/charm/update.html"


class BattleScarDetailView(DetailView):
    model = BattleScar
    template_name = "wod/characters/werewolf/battlescar/detail.html"


class BattleScarCreateView(CreateView):
    model = BattleScar
    fields = "__all__"
    template_name = "wod/characters/werewolf/battlescar/create.html"


class BattleScarUpdateView(UpdateView):
    model = BattleScar
    fields = "__all__"
    template_name = "wod/characters/werewolf/battlescar/update.html"
