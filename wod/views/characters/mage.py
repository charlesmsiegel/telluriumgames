from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View
from game.models.chronicle import Chronicle

from wod.forms.characters.mage import MageAbilitiesForm, MageAdvantagesForm, MageAttributeForm, MageCreationForm, MageForm, ResonanceForm
from wod.models.characters.human import Archetype, MeritFlawRating
from wod.models.characters.mage.cabal import Cabal
from wod.models.characters.mage.faction import MageFaction
from wod.models.characters.mage.focus import Instrument, Paradigm, Practice
from wod.models.characters.mage.mage import Mage, Rote
from wod.models.characters.mage.resonance import Resonance, ResRating
from wod.models.characters.mage.rote import Effect
from wod.models.characters.mage.utils import PRIMARY_ABILITIES


def load_factions(request):
    affiliation_id = request.GET.get("affiliation")
    factions = MageFaction.objects.filter(parent=affiliation_id).order_by("name")
    return render(
        request,
        "wod/characters/mage/mage/load_faction_dropdown_list.html",
        {"factions": factions},
    )


def load_subfactions(request):
    faction_id = request.GET.get("faction")
    subfactions = MageFaction.objects.filter(parent=faction_id).order_by("name")
    return render(
        request,
        "wod/characters/mage/mage/load_subfaction_dropdown_list.html",
        {"subfactions": subfactions},
    )

class MageCreateView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context["form"] = MageCreationForm()
        return render(request, "wod/characters/mage/mage/create.html", context)

    def post(self, request, *args, **kwargs):
        form = MageCreationForm(request.POST)
        chron = None
        affiliation = None
        faction = None
        subfaction = None
        print(form.data)
        print(form.data['affiliation'])
        if "chronicle" in form.data.keys():
            chron = Chronicle.objects.filter(pk=form.data["chronicle"]).first()
        if "affiliation" in form.data.keys():
            affiliation = MageFaction.objects.filter(pk=form.data["affiliation"]).first()
        if "faction" in form.data.keys():
            faction = MageFaction.objects.filter(pk=form.data["faction"]).first()
        if "subfaction" in form.data.keys():
            subfaction = MageFaction.objects.filter(pk=form.data["subfaction"]).first()
        s = Mage.objects.create(
            name=form.data["name"],
            concept=form.data["concept"],
            demeanor=Archetype.objects.get(pk=form.data["demeanor"]),
            nature=Archetype.objects.get(pk=form.data["nature"]),
            owner=request.user,
            status="Un",
            essence=1,
            chronicle=chron,
            affiliation=affiliation,
            faction=faction,
            subfaction=subfaction,
        )
        return redirect(s.get_absolute_url())

class MageDetailView(View):
    def get(self, request, *args, **kwargs):
        mage = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(mage)
        if mage.status != "Un":
            return render(request, "wod/characters/mage/mage/detail.html", context,)
        if mage.creation_status == 1:
            context["form"] = MageAttributeForm(initial=mage.get_attributes())
            return render(
                request,
                "wod/characters/mage/mage/creation_attribute.html",
                context,
            )
        if mage.creation_status == 2:
            d = mage.get_abilities()
            context["form"] = MageAbilitiesForm(initial=d, character=mage)
            return render(
                request,
                "wod/characters/mage/mage/creation_abilities.html",
                context,
            )
        if mage.creation_status == 3:
            d = mage.get_backgrounds()
            d['arete'] = 1
            context["form"] = MageAdvantagesForm(initial=d, character=mage)
            return render(
                request,
                "wod/characters/mage/mage/creation_advantages.html",
                context,
            )
        # if mage.creation_status == 4:
        #     context["form"] = ExaltedCharmForm(character=char)
        #     return render(
        #         request,
        #         "wod/characters/mage/mage/creation_charms.html",
        #         context,
        #     )
        # if mage.creation_status == 5:
        #     context["form"] = ExaltedIntimacyForm()
        #     return render(
        #         request,
        #         "wod/characters/mage/mage/creation_intimacies.html",
        #         context,
        #     )
        # if mage.creation_status == 6:
        #     return render(
        #         request,
        #         "wod/characters/mage/mage/creation_bonus_points.html",
        #         context,
        #     )
        return render(request, "wod/characters/mage/mage/detail.html", context,)

    def post(self, request, *args, **kwargs):
        char = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)
        if char.creation_status == 1:
            form = MageAttributeForm(request.POST)
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
                context["form"] = MageAbilitiesForm(initial=d, character=char)
                return render(
                    request,
                    "wod/characters/mage/mage/creation_abilities.html",
                    context,
                )
            context["form"] = MageAttributeForm(initial=char.get_attributes())
            return render(
                request,
                "wod/characters/mage/mage/creation_attribute.html",
                context,
            )
        if char.creation_status == 2:
            form = MageAbilitiesForm(request.POST, character=char)
            if form.has_abilities():
                form.full_clean()
                for key in list(char.get_talents().keys()) + list(char.get_skills().keys()) + list(char.get_knowledges().keys()):
                    setattr(char, key, form.cleaned_data[key])
                char.creation_status += 1
                char.save()
                context["form"] = MageAdvantagesForm()
                return render(
                    request,
                    "wod/characters/mage/mage/creation_advantages.html",
                    context,
                )
            d = char.get_abilities()
            context["form"] = MageAbilitiesForm(initial=d, character=char)
            return render(
                request,
                "wod/characters/mage/mage/creation_abilities.html",
                context,
            )
        # if char.creation_status == 3:
        #     form = ExaltedMeritsForm(request.POST)
        #     if form.has_merits(char):
        #         form.full_clean()
        #         merits = [form.cleaned_data[f"merit_{i}"] for i in range(1, 11)]
        #         merit_ratings = [
        #             form.cleaned_data[f"merit_{i}_rating"] for i in range(1, 11)
        #         ]
        #         pairs = list(zip(merits, merit_ratings))
        #         pairs = [x for x in pairs if x[0] != "----"]
        #         pairs = [(ExMerit.objects.get(name=x[0]), x[1]) for x in pairs]
        #         pairs = [(x[0], x[1]) for x in pairs if x[1] in x[0].ratings]
        #         for merit, rating in pairs:
        #             MeritRating.objects.create(
        #                 character=char, merit=merit, rating=rating
        #             )
        #         char.creation_status += 1
        #         char.save()
        #         context["form"] = ExaltedCharmForm(character=char)
        #         return render(
        #             request,
        #             "exalted/characters/solars/solar/creation_charms.html",
        #             context,
        #         )
        #     d = char.get_abilities()
        #     context["form"] = ExaltedMeritsForm()
        #     return render(
        #         request,
        #         "exalted/characters/solars/solar/creation_merits.html",
        #         context,
        #     )
        # if char.creation_status == 4:
        #     form = ExaltedCharmForm(request.POST, character=char)
        #     form.full_clean()
        #     charm_name = form.cleaned_data["charm"]
        #     c = Charm.objects.get(name=charm_name)
        #     char.add_charm(c)
        #     if char.has_charms():
        #         char.creation_status += 1
        #         char.save()
        #         context["form"] = ExaltedIntimacyForm()
        #         return render(
        #             request,
        #             "exalted/characters/solars/solar/creation_intimacies.html",
        #             context,
        #         )
        #     context["form"] = ExaltedCharmForm(character=char)
        #     return render(
        #         request,
        #         "exalted/characters/solars/solar/creation_charms.html",
        #         context,
        #     )
        # if char.creation_status == 5:
        #     form = ExaltedIntimacyForm(request.POST)
        #     if form.has_intimacies():
        #         form.full_clean()
        #         i1 = Intimacy.objects.create(
        #             name=form.cleaned_data["intimacy_1"],
        #             intimacy_type=form.cleaned_data["intimacy_type_1"],
        #             strength=form.cleaned_data["intimacy_strength_1"],
        #             is_negative=form.cleaned_data["is_negative_1"],
        #         )
        #         i2 = Intimacy.objects.create(
        #             name=form.cleaned_data["intimacy_2"],
        #             intimacy_type=form.cleaned_data["intimacy_type_2"],
        #             strength=form.cleaned_data["intimacy_strength_2"],
        #             is_negative=form.cleaned_data["is_negative_2"],
        #         )
        #         i3 = Intimacy.objects.create(
        #             name=form.cleaned_data["intimacy_3"],
        #             intimacy_type=form.cleaned_data["intimacy_type_3"],
        #             strength=form.cleaned_data["intimacy_strength_3"],
        #             is_negative=form.cleaned_data["is_negative_3"],
        #         )
        #         i4 = Intimacy.objects.create(
        #             name=form.cleaned_data["intimacy_4"],
        #             intimacy_type=form.cleaned_data["intimacy_type_4"],
        #             strength=form.cleaned_data["intimacy_strength_4"],
        #             is_negative=form.cleaned_data["is_negative_4"],
        #         )
        #         char.add_intimacy(i1)
        #         char.add_intimacy(i2)
        #         char.add_intimacy(i3)
        #         char.add_intimacy(i4)
        #         char.limit_trigger = form.cleaned_data["limit_trigger"]
        #         char.creation_status += 1
        #         char.save()
        #         char.apply_finishing_touches()
        #         # TODO: Form for Bonus Points
        #         return render(
        #             request,
        #             "exalted/characters/solars/solar/creation_bonus_points.html",
        #             context,
        #         )
        #     context["form"] = ExaltedIntimacyForm()
        #     return render(
        #         request,
        #         "exalted/characters/solars/solar/creation_intimacies.html",
        #         context,
        #     )
        # if char.creation_status == 6:
        #     pass

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
        all_effects = list(Rote.objects.filter(mage=context["object"]))
        # all_effects = list(context["object"].effects.all())
        row_length = 2
        all_effects = [
            all_effects[i : i + row_length]
            for i in range(0, len(all_effects), row_length)
        ]
        context["rotes"] = all_effects

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


# class MageCreateView(CreateView):
#     model = Mage
#     form_class = MageForm
#     template_name = "wod/characters/mage/mage/form.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["resform"] = ResonanceForm(data_list=Resonance.objects.all())
#         return context


class MageUpdateView(UpdateView):
    model = Mage
    fields = "__all__"
    template_name = "wod/characters/mage/mage/form.html"


class CabalDetailView(DetailView):
    model = Cabal
    template_name = "wod/characters/mage/cabal/detail.html"


class CabalCreateView(CreateView):
    model = Cabal
    fields = "__all__"
    template_name = "wod/characters/mage/cabal/form.html"


class CabalUpdateView(UpdateView):
    model = Cabal
    fields = "__all__"
    template_name = "wod/characters/mage/cabal/form.html"


class InstrumentDetailView(DetailView):
    model = Instrument
    template_name = "wod/characters/mage/instrument/detail.html"


class InstrumentCreateView(CreateView):
    model = Instrument
    fields = ["name", "description"]
    template_name = "wod/characters/mage/instrument/form.html"


class InstrumentUpdateView(UpdateView):
    model = Instrument
    fields = ["name", "description"]
    template_name = "wod/characters/mage/instrument/form.html"


class MageFactionDetailView(View):
    def get(self, request, *args, **kwargs):
        magefaction = MageFaction.objects.get(pk=kwargs["pk"])
        context = self.get_context(magefaction)
        return render(request, "wod/characters/mage/magefaction/detail.html", context)

    def get_context(self, magefaction):
        context = {}
        context["object"] = magefaction
        context["languages"] = ", ".join([str(x) for x in magefaction.languages.all()])
        context["affinities"] = ", ".join([x.title() for x in magefaction.affinities])
        context["paradigms"] = ", ".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in magefaction.paradigms.all()
            ]
        )
        context["practices"] = ", ".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in magefaction.practices.all()
            ]
        )
        context["media"] = ", ".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in magefaction.media.all()
            ]
        )
        context["materials"] = ", ".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in magefaction.materials.all()
            ]
        )
        context["year"] = abs(magefaction.founded)
        context["subfactions"] = ", ".join(
            [
                f'<a href="{x.get_absolute_url()}">{x}</a>'
                for x in MageFaction.objects.filter(parent=magefaction)
            ]
        )
        return context


class MageFactionCreateView(CreateView):
    model = MageFaction
    fields = "__all__"
    template_name = "wod/characters/mage/magefaction/form.html"


class MageFactionUpdateView(UpdateView):
    model = MageFaction
    fields = "__all__"
    template_name = "wod/characters/mage/magefaction/form.html"


class ParadigmDetailView(DetailView):
    model = Paradigm
    template_name = "wod/characters/mage/paradigm/detail.html"


class ParadigmCreateView(CreateView):
    model = Paradigm
    fields = ["name", "practices", "description"]
    template_name = "wod/characters/mage/paradigm/form.html"


class ParadigmUpdateView(UpdateView):
    model = Paradigm
    fields = ["name", "practices", "description"]
    template_name = "wod/characters/mage/paradigm/form.html"


class PracticeDetailView(DetailView):
    model = Practice
    template_name = "wod/characters/mage/practice/detail.html"


class PracticeCreateView(CreateView):
    model = Practice
    fields = ["name", "abilities", "instruments", "description"]
    template_name = "wod/characters/mage/practice/form.html"


class PracticeUpdateView(UpdateView):
    model = Practice
    fields = ["name", "abilities", "instruments", "description"]
    template_name = "wod/characters/mage/practice/form.html"


class ResonanceDetailView(DetailView):
    model = Resonance
    template_name = "wod/characters/mage/resonance/detail.html"


class ResonanceCreateView(CreateView):
    model = Resonance
    fields = [
        "name",
        "correspondence",
        "life",
        "prime",
        "entropy",
        "matter",
        "spirit",
        "forces",
        "mind",
        "time",
    ]
    template_name = "wod/characters/mage/resonance/form.html"


class ResonanceUpdateView(UpdateView):
    model = Resonance
    fields = [
        "name",
        "correspondence",
        "life",
        "prime",
        "entropy",
        "matter",
        "spirit",
        "forces",
        "mind",
        "time",
    ]
    template_name = "wod/characters/mage/resonance/form.html"


class EffectDetailView(DetailView):
    model = Effect
    template_name = "wod/characters/mage/effect/detail.html"


class EffectCreateView(CreateView):
    model = Effect
    fields = "__all__"
    template_name = "wod/characters/mage/effect/form.html"


class EffectUpdateView(UpdateView):
    model = Effect
    fields = "__all__"
    template_name = "wod/characters/mage/effect/form.html"


class RoteDetailView(DetailView):
    model = Rote
    template_name = "wod/characters/mage/rote/detail.html"


class RoteCreateView(CreateView):
    model = Rote
    fields = "__all__"
    template_name = "wod/characters/mage/rote/form.html"


class RoteUpdateView(UpdateView):
    model = Rote
    fields = "__all__"
    template_name = "wod/characters/mage/rote/form.html"
