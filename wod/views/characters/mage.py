from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, View

from wod.forms import MageForm
from wod.models.characters.human import MeritFlawRating
from wod.models.characters.mage.faction import MageFaction
from wod.models.characters.mage.focus import Instrument, Paradigm, Practice
from wod.models.characters.mage.mage import Cabal, Mage
from wod.models.characters.mage.resonance import Resonance, ResRating
from wod.models.characters.mage.rote import Effect
from wod.models.characters.mage.utils import PRIMARY_ABILITIES


def load_factions(request):
    affiliation_id = request.GET.get("affiliation")
    factions = MageFaction.objects.filter(parent=affiliation_id).order_by("name")
    return render(
        request,
        "wod/characters/mage/load_faction_dropdown_list.html",
        {"factions": factions},
    )


def load_subfactions(request):
    faction_id = request.GET.get("faction")
    subfactions = MageFaction.objects.filter(parent=faction_id).order_by("name")
    return render(
        request,
        "wod/characters/mage/load_subfaction_dropdown_list.html",
        {"subfactions": subfactions},
    )


class MageDetailView(View):
    def get(self, request, *args, **kwargs):
        mage = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(mage)
        return render(request, "wod/characters/mage/mage/detail.html", context)

    def get_context(self, mage):
        context = {"object": mage}
        specialties = {}
        for attribute in mage.get_attributes():
            specialties[attribute] = ", ".join(
                [x.name for x in mage.specialties.filter(stat=attribute)]
            )
        for ability in mage.get_abilities():
            specialties[ability] = ", ".join(
                [x.name for x in mage.specialties.filter(stat=ability)]
            )
        for sphere in mage.get_spheres():
            specialties[sphere] = ", ".join(
                [x.name for x in mage.specialties.filter(stat=sphere)]
            )
        for key, value in specialties.items():
            context[f"{key}_spec"] = value

        context["resonance"] = ResRating.objects.filter(mage=mage).order_by(
            "resonance__name"
        )
        context["merits_and_flaws"] = MeritFlawRating.objects.order_by(
            "mf__name"
        ).filter(character=mage)
        all_effects = list(context["object"].effects.all())
        row_length = 2
        all_effects = [
            all_effects[i : i + row_length] for i in range(0, len(all_effects), row_length)
        ]
        context["effects"] = all_effects

        secondary_talents = [
            [f"{k.replace('_', ' ').title()}", v, context[f"{k}_spec"]]
            for k, v in mage.get_talents().items()
            if k not in PRIMARY_ABILITIES and v != 0
        ]
        secondary_skills = [
            [f"{k.replace('_', ' ').title()}", v, context[f"{k}_spec"]]
            for k, v in mage.get_skills().items()
            if k not in PRIMARY_ABILITIES and v != 0
        ]
        secondary_knowledges = [
            [f"{k.replace('_', ' ').title()}", v, context[f"{k}_spec"]]
            for k, v in mage.get_knowledges().items()
            if k not in PRIMARY_ABILITIES and v != 0
        ]

        for triple in secondary_knowledges:
            if triple[0] == "History Knowledge":
                triple[0] = "History"

        secondary_talents.sort(key=lambda x: x[0])
        secondary_skills.sort(key=lambda x: x[0])
        secondary_knowledges.sort(key=lambda x: x[0])
        num_sec_tal = len(secondary_talents)
        num_sec_ski = len(secondary_skills)
        num_sec_kno = len(secondary_knowledges)
        m = max(num_sec_tal, num_sec_ski, num_sec_kno)
        for _ in range(m - num_sec_tal):
            secondary_talents.append(("", 0, []))
        for _ in range(m - num_sec_ski):
            secondary_skills.append(("", 0, []))
        for _ in range(m - num_sec_kno):
            secondary_knowledges.append(("", 0, []))
        context["secondaries"] = list(
            zip(secondary_talents, secondary_skills, secondary_knowledges)
        )
        return context


class MageCreateView(CreateView):
    model = Mage
    form_class = MageForm
    # fields = "__all__"
    template_name = "wod/characters/mage/mage/create.html"


class MageUpdateView(UpdateView):
    model = Mage
    fields = "__all__"
    template_name = "wod/characters/mage/mage/update.html"


class CabalDetailView(DetailView):
    model = Cabal
    template_name = "wod/characters/mage/cabal/detail.html"


class CabalCreateView(CreateView):
    model = Cabal
    fields = "__all__"
    template_name = "wod/characters/mage/cabal/create.html"


class CabalUpdateView(UpdateView):
    model = Cabal
    fields = "__all__"
    template_name = "wod/characters/mage/cabal/update.html"


class InstrumentDetailView(DetailView):
    model = Instrument
    template_name = "wod/characters/mage/instrument/detail.html"


class InstrumentCreateView(CreateView):
    model = Instrument
    fields = "__all__"
    template_name = "wod/characters/mage/instrument/create.html"


class InstrumentUpdateView(UpdateView):
    model = Instrument
    fields = "__all__"
    template_name = "wod/characters/mage/instrument/update.html"


class MageFactionDetailView(DetailView):
    model = MageFaction
    template_name = "wod/characters/mage/magefaction/detail.html"


class MageFactionCreateView(CreateView):
    model = MageFaction
    fields = "__all__"
    template_name = "wod/characters/mage/magefaction/create.html"


class MageFactionUpdateView(UpdateView):
    model = MageFaction
    fields = "__all__"
    template_name = "wod/characters/mage/magefaction/update.html"


class ParadigmDetailView(DetailView):
    model = Paradigm
    template_name = "wod/characters/mage/paradigm/detail.html"


class ParadigmCreateView(CreateView):
    model = Paradigm
    fields = "__all__"
    template_name = "wod/characters/mage/paradigm/create.html"


class ParadigmUpdateView(UpdateView):
    model = Paradigm
    fields = "__all__"
    template_name = "wod/characters/mage/paradigm/update.html"


class PracticeDetailView(DetailView):
    model = Practice
    template_name = "wod/characters/mage/practice/detail.html"


class PracticeCreateView(CreateView):
    model = Practice
    fields = "__all__"
    template_name = "wod/characters/mage/practice/create.html"


class PracticeUpdateView(UpdateView):
    model = Practice
    fields = "__all__"
    template_name = "wod/characters/mage/practice/update.html"


class ResonanceDetailView(DetailView):
    model = Resonance
    template_name = "wod/characters/mage/resonance/detail.html"


class ResonanceCreateView(CreateView):
    model = Resonance
    fields = "__all__"
    template_name = "wod/characters/mage/resonance/create.html"


class ResonanceUpdateView(UpdateView):
    model = Resonance
    fields = "__all__"
    template_name = "wod/characters/mage/resonance/update.html"


class EffectDetailView(DetailView):
    model = Effect
    template_name = "wod/characters/mage/effect/detail.html"


class EffectCreateView(CreateView):
    model = Effect
    fields = "__all__"
    template_name = "wod/characters/mage/effect/create.html"


class EffectUpdateView(UpdateView):
    model = Effect
    fields = "__all__"
    template_name = "wod/characters/mage/effect/update.html"
