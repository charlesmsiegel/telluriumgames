from django.forms import formset_factory
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from core.models import Language
from game.models.chronicle import Chronicle
from wod.forms.characters.mage import (
    MageAbilitiesForm,
    MageAdvantagesForm,
    MageAttributeForm,
    MageCreationForm,
    MageDescriptionForm,
    MageFreebieForm,
    MageMeritFlawForm,
    MagePowersForm,
)
from wod.models.characters.human import Archetype, MeritFlaw, MeritFlawRating
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


def load_mf_ratings(request):
    mf_id = request.GET.get("mf")
    ratings = MeritFlaw.objects.get(pk=mf_id).ratings
    return render(
        request,
        "wod/characters/mage/mage/load_mf_rating_dropdown_list.html",
        {"ratings": ratings},
    )


class MageCreateView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context["form"] = MageCreationForm()
        return render(request, "wod/characters/mage/mage/create.html", context)

    def post(self, request, *args, **kwargs):
        if "Full Random" in request.POST:
            s = Mage.objects.create(owner=request.user, status="Un")
            s.random()
            return redirect(s.get_absolute_url())
        elif "Random Basics" in request.POST:
            s = Mage.objects.create(owner=request.user, status="Un")
            s.random_name()
            s.random_concept()
            s.random_archetypes()
            s.random_essence()
            s.random_faction()
            s.save()
            return redirect(s.get_absolute_url())
        elif "Save" in request.POST:
            form = MageCreationForm(request.POST)
            chron = None
            affiliation = None
            faction = None
            subfaction = None
            if "chronicle" in form.data.keys():
                chron = Chronicle.objects.filter(pk=form.data["chronicle"]).first()
            if "affiliation" in form.data.keys():
                affiliation = MageFaction.objects.filter(
                    pk=form.data["affiliation"]
                ).first()
            if "faction" in form.data.keys():
                faction = MageFaction.objects.filter(pk=form.data["faction"]).first()
            if "subfaction" in form.data.keys():
                subfaction = MageFaction.objects.filter(
                    pk=form.data["subfaction"]
                ).first()
            s = Mage.objects.create(
                name=form.data["name"],
                concept=form.data["concept"],
                demeanor=Archetype.objects.get(pk=form.data["demeanor"]),
                nature=Archetype.objects.get(pk=form.data["nature"]),
                owner=request.user,
                status="Un",
                chronicle=chron,
                affiliation=affiliation,
                faction=faction,
                subfaction=subfaction,
            )
            return redirect(s.get_absolute_url())
        context = {}
        context["form"] = MageCreationForm()
        render(request, "wod/characters/mage/mage/create.html", context)


class MageDetailView(View):
    def get(self, request, *args, **kwargs):
        mage = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(mage)
        if mage.status != "Un":
            return render(request, "wod/characters/mage/mage/detail.html", context,)
        if mage.creation_status == 1:
            context["form"] = MageAttributeForm(initial=mage.get_attributes())
            return render(
                request, "wod/characters/mage/mage/creation_attribute.html", context,
            )
        if mage.creation_status == 2:
            d = mage.get_abilities()
            context["form"] = MageAbilitiesForm(initial=d, character=mage)
            return render(
                request, "wod/characters/mage/mage/creation_abilities.html", context,
            )
        if mage.creation_status == 3:
            d = mage.get_backgrounds()
            d["arete"] = 1
            context["form"] = MageAdvantagesForm(initial=d, character=mage)
            return render(
                request, "wod/characters/mage/mage/creation_advantages.html", context,
            )
        if mage.creation_status == 4:
            d = mage.get_spheres()
            context["form"] = MagePowersForm(initial=d, character=mage)
            return render(
                request, "wod/characters/mage/mage/creation_powers.html", context,
            )
        if mage.creation_status == 5:
            d = mage.get_attributes()
            d.update(mage.get_abilities())
            d.update(mage.get_backgrounds())
            d.update(mage.get_spheres())
            d["willpower"] = 5
            d["native_language"] = Language.objects.get(name="English")
            MFFormset = formset_factory(MageMeritFlawForm, extra=1)
            context["formset"] = MFFormset()
            context["form"] = MageFreebieForm(initial=d, character=mage)
            return render(
                request, "wod/characters/mage/mage/creation_freebies.html", context,
            )
        if mage.creation_status == 6:
            context["form"] = MageDescriptionForm(character=mage)
            return render(
                request, "wod/characters/mage/mage/creation_description.html", context,
            )
        return render(request, "wod/characters/mage/mage/detail.html", context,)

    def post(self, request, *args, **kwargs):
        char = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)
        if char.creation_status == 1:
            form = MageAttributeForm(request.POST)
            if "Random Attributes" in form.data:
                char.random_attributes()
                char.creation_status += 1
                char.save()
                d = char.get_abilities()
                context["form"] = MageAbilitiesForm(initial=d, character=char)
                return render(
                    request,
                    "wod/characters/mage/mage/creation_abilities.html",
                    context,
                )
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
                request, "wod/characters/mage/mage/creation_attribute.html", context,
            )
        if char.creation_status == 2:
            form = MageAbilitiesForm(request.POST, character=char)
            if "Random Abilities" in form.data:
                char.random_abilities()
                char.creation_status += 1
                char.save()
                d = char.get_backgrounds()
                d["arete"] = 1
                d["affinity_sphere"] = char.affinity_sphere
                d["paradigms"] = char.paradigms.all()
                d["practices"] = char.practices.all()
                d["instruments"] = char.instruments.all()
                context["form"] = MageAdvantagesForm(initial=d, character=char)
                return render(
                    request,
                    "wod/characters/mage/mage/creation_advantages.html",
                    context,
                )
            if form.has_abilities():
                form.full_clean()
                for key in (
                    list(char.get_talents().keys())
                    + list(char.get_skills().keys())
                    + list(char.get_knowledges().keys())
                ):
                    if key == "do" and char.faction.name != "Akashayana":
                        pass
                    else:
                        setattr(char, key, form.cleaned_data[key])
                char.creation_status += 1
                char.save()
                d = char.get_backgrounds()
                d["arete"] = 1
                d["affinity_sphere"] = char.affinity_sphere
                d["paradigms"] = char.paradigms.all()
                d["practices"] = char.practices.all()
                d["instruments"] = char.instruments.all()
                context["form"] = MageAdvantagesForm(initial=d, character=char)
                return render(
                    request,
                    "wod/characters/mage/mage/creation_advantages.html",
                    context,
                )
            d = char.get_abilities()
            context["form"] = MageAbilitiesForm(initial=d, character=char)
            return render(
                request, "wod/characters/mage/mage/creation_abilities.html", context,
            )
        if char.creation_status == 3:
            form = MageAdvantagesForm(request.POST, character=char)
            if "Random Advantages" in form.data:
                char.random_focus()
                char.random_backgrounds()
                char.random_arete()
                char.random_affinity_sphere()
                char.creation_status += 1
                char.save()
                d = char.get_spheres()
                context["form"] = MagePowersForm(initial=d, character=char)
                return render(
                    request, "wod/characters/mage/mage/creation_powers.html", context,
                )
            if form.complete():
                form.full_clean()
                for key in char.get_backgrounds().keys():
                    setattr(char, key, form.cleaned_data[key])
                char.arete = form.cleaned_data["arete"]
                char.affinity_sphere = form.cleaned_data["affinity_sphere"]
                setattr(char, char.affinity_sphere, 1)
                char.paradigms.add(*list(form.cleaned_data["paradigms"]))
                char.practices.add(*list(form.cleaned_data["practices"]))
                char.instruments.add(*list(form.cleaned_data["instruments"]))
                char.creation_status += 1
                char.save()
                d = char.get_spheres()
                context["form"] = MagePowersForm(initial=d, character=char)
                return render(
                    request, "wod/characters/mage/mage/creation_powers.html", context,
                )
            d = char.get_backgrounds()
            d["arete"] = 1
            d["affinity_sphere"] = char.affinity_sphere
            d["paradigms"] = char.paradigms.all()
            d["practices"] = char.practices.all()
            d["instruments"] = char.instruments.all()
            context["form"] = MageAdvantagesForm(initial=d, character=char)
            return render(
                request, "wod/characters/mage/mage/creation_advantages.html", context,
            )
        if char.creation_status == 4:
            form = MagePowersForm(request.POST, character=char)
            if "Random Powers" in form.data:
                char.random_spheres()
                char.random_resonance()
                char.creation_status += 1
                char.save()
                d = char.get_attributes()
                d.update(char.get_abilities())
                d.update(char.get_backgrounds())
                d.update(char.get_spheres())
                d["willpower"] = 5
                d["native_language"] = Language.objects.get(name="English")
                MFFormset = formset_factory(MageMeritFlawForm, extra=1)
                context["formset"] = MFFormset()
                context["form"] = MageFreebieForm(initial=d, character=char)
                return render(
                    request, "wod/characters/mage/mage/creation_freebies.html", context,
                )
            form.full_clean()
            if form.complete():
                for key in char.get_spheres().keys():
                    setattr(char, key, form.cleaned_data[key])
                res = form.cleaned_data["resonance"]
                char.add_resonance(res.name)
                char.creation_status += 1
                char.save()
                d = char.get_attributes()
                d.update(char.get_abilities())
                d.update(char.get_backgrounds())
                d.update(char.get_spheres())
                d["willpower"] = 5
                d["native_language"] = Language.objects.get(name="English")
                MFFormset = formset_factory(MageMeritFlawForm, extra=1)
                context["formset"] = MFFormset()
                context["form"] = MageFreebieForm(initial=d, character=char)
                return render(
                    request, "wod/characters/mage/mage/creation_freebies.html", context,
                )
            d = char.get_spheres()
            context["form"] = MagePowersForm(initial=d, character=char)
            return render(
                request, "wod/characters/mage/mage/creation_powers.html", context,
            )
        if char.creation_status == 5:
            form = MageFreebieForm(request.POST, character=char)
            if "Random Freebies" in form.data:
                char.random_freebies()
                char.creation_status += 1
                char.save()
                context["form"] = MageDescriptionForm(character=char)
                return render(
                    request,
                    "wod/characters/mage/mage/creation_description.html",
                    context,
                )
            form.full_clean()
            if form.complete():
                for key in list(char.get_attributes().keys()):
                    setattr(char, key, form.cleaned_data[key])
                for key in (
                    list(char.get_talents().keys())
                    + list(char.get_skills().keys())
                    + list(char.get_knowledges().keys())
                ):
                    if char.faction.name == "Akashayana" or key != "do":
                        setattr(char, key, form.cleaned_data[key])
                for key in list(char.get_spheres().keys()):
                    setattr(char, key, form.cleaned_data[key])
                for key in list(char.get_backgrounds().keys()):
                    setattr(char, key, form.cleaned_data[key])
                char.willpower = form.data["willpower"]
                mf_keys = [
                    x
                    for x in form.data.keys()
                    if x.startswith("form-")
                    and (x.endswith("-mf") or x.endswith("-rating"))
                ]
                mf_values = [int(form.data[x]) for x in mf_keys]
                mfs = dict(zip(mf_keys, mf_values))
                num_mf = len(mfs) // 2
                new_mfs = {}
                for i in range(num_mf):
                    new_mfs[mfs[f"form-{i}-mf"]] = mfs[f"form-{i}-rating"]
                for key, value in new_mfs.items():
                    char.add_mf(MeritFlaw.objects.get(pk=key), value)
                char.languages.add(form.data["native_language"])
                char.languages.add(*form.data["languages"])
                char.creation_status += 1
                char.save()
                context["form"] = MageDescriptionForm(character=char)
                return render(
                    request,
                    "wod/characters/mage/mage/creation_description.html",
                    context,
                )
            d = char.get_attributes()
            d.update(char.get_abilities())
            d.update(char.get_backgrounds())
            d.update(char.get_spheres())
            d["willpower"] = 5
            d["native_language"] = Language.objects.get(name="English")
            MFFormset = formset_factory(MageMeritFlawForm, extra=1)
            context["formset"] = MFFormset()
            context["form"] = MageFreebieForm(initial=d, character=char)
            return render(
                request, "wod/characters/mage/mage/creation_freebies.html", context,
            )
        if char.creation_status == 6:
            form = MageDescriptionForm(request.POST, character=char)
            if "Random Description" in form.data:
                char.update_status("Sub")
                char.random_history()
                char.random_mage_history()
                char.mf_based_corrections()
                char.creation_status += 1
                char.save()
                return render(request, "wod/characters/mage/mage/detail.html", context,)
            form.full_clean()
            if form.complete():
                for key, value in form.cleaned_data.items():
                    setattr(char, key, value)
                char.creation_status += 1
                char.save()
                return render(request, "wod/characters/mage/mage/detail.html", context,)
            context["form"] = MageDescriptionForm(character=char)
            return render(
                request, "wod/characters/mage/mage/creation_description.html", context,
            )
        return render(request, "wod/characters/mage/mage/detail.html", context,)

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
