from django.forms import formset_factory
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from core.models import Language
from game.models import Chronicle, Scene
from wod.forms.characters.human import AttributeForm, MeritFlawForm
from wod.forms.characters.mage import (
    MageAbilitiesForm,
    MageAdvantagesForm,
    MageCreationForm,
    MageDescriptionForm,
    MageFreebieForm,
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
        if "Random Basics" in request.POST:
            s = Mage.objects.create(owner=request.user, status="Un")
            s.random_name()
            s.random_concept()
            s.random_archetypes()
            s.random_essence()
            s.random_faction()
            s.save()
            return redirect(s.get_absolute_url())
        if "Save" in request.POST:
            form = MageCreationForm(request.POST)
            form.full_clean()
            affiliation = None
            faction = None
            subfaction = None
            if "affiliation" in form.data.keys():
                affiliation = form.cleaned_data["affiliation"]
            if "faction" in form.data.keys():
                faction = form.cleaned_data["faction"]
            if "subfaction" in form.data.keys():
                subfaction = form.cleaned_data["subfaction"]
            s = Mage.objects.create(
                name=form.data["name"],
                concept=form.data["concept"],
                demeanor=form.cleaned_data["demeanor"],
                nature=form.cleaned_data["nature"],
                owner=request.user,
                status="Un",
                chronicle=form.cleaned_data["chronicle"],
                affiliation=affiliation,
                faction=faction,
                subfaction=subfaction,
            )
            return redirect(s.get_absolute_url())
        context = {}
        context["form"] = MageCreationForm()
        return render(request, "wod/characters/mage/mage/create.html", context)


class MageDetailView(View):
    def get(self, request, *args, **kwargs):
        mage = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(mage)
        if mage.status != "Un":
            return render(request, "wod/characters/mage/mage/detail.html", context,)
        if mage.creation_status == 1:
            context["form"] = AttributeForm(character=mage)
            return render(
                request, "wod/characters/mage/mage/1_attribute.html", context,
            )
        if mage.creation_status == 2:
            context["form"] = MageAbilitiesForm(character=mage)
            return render(
                request, "wod/characters/mage/mage/2_abilities.html", context,
            )
        if mage.creation_status == 3:
            context["form"] = MageAdvantagesForm(character=mage)
            return render(
                request, "wod/characters/mage/mage/3_advantages.html", context,
            )
        if mage.creation_status == 4:
            context["resonances"] = Resonance.objects.all().order_by("name")
            context["form"] = MagePowersForm(character=mage)
            return render(request, "wod/characters/mage/mage/4_powers.html", context,)
        if mage.creation_status == 5:
            MFFormset = formset_factory(MeritFlawForm, extra=1)
            context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
            context["form"] = MageFreebieForm(character=mage)
            return render(request, "wod/characters/mage/mage/5_freebies.html", context,)
        if mage.creation_status == 6:
            context["form"] = MageDescriptionForm(character=mage)
            return render(
                request, "wod/characters/mage/mage/6_description.html", context,
            )
        return render(request, "wod/characters/mage/mage/detail.html", context,)

    def post(self, request, *args, **kwargs):
        char = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)
        if char.creation_status == 1:
            form = AttributeForm(request.POST, character=char)
            if "Random Attributes" in form.data:
                char.random_attributes()
                char.next_stage()
                context["form"] = MageAbilitiesForm(character=char)
                return render(
                    request, "wod/characters/mage/mage/2_abilities.html", context,
                )
            form.assign()
            if char.has_attributes():
                char.next_stage()
                context["form"] = MageAbilitiesForm(character=char)
                return render(
                    request, "wod/characters/mage/mage/2_abilities.html", context,
                )
            context["form"] = AttributeForm(character=char)
            return render(
                request, "wod/characters/mage/mage/1_attribute.html", context,
            )
        if char.creation_status == 2:
            form = MageAbilitiesForm(request.POST, character=char)
            if "Back" in form.data:
                char.prev_stage()
                context["form"] = AttributeForm(character=char)
                return render(
                    request, "wod/characters/mage/mage/1_attribute.html", context,
                )
            if "Random Abilities" in form.data:
                char.random_abilities()
                char.next_stage()
                context["form"] = MageAdvantagesForm(character=char)
                return render(
                    request, "wod/characters/mage/mage/3_advantages.html", context,
                )
            form.assign()
            if char.has_abilities():
                char.next_stage()
                context["form"] = MageAdvantagesForm(character=char)
                return render(
                    request, "wod/characters/mage/mage/3_advantages.html", context,
                )
            context["form"] = MageAbilitiesForm(character=char)
            return render(
                request, "wod/characters/mage/mage/2_abilities.html", context,
            )
        if char.creation_status == 3:
            form = MageAdvantagesForm(request.POST, character=char)
            if "Back" in form.data:
                char.prev_stage()
                context["form"] = MageAbilitiesForm(character=char)
                return render(
                    request, "wod/characters/mage/mage/2_abilities.html", context,
                )
            if "Random Advantages" in form.data:
                char.random_focus()
                char.random_backgrounds()
                char.random_arete()
                char.random_affinity_sphere()
                char.next_stage()
                context["resonances"] = Resonance.objects.all().order_by("name")
                context["form"] = MagePowersForm(character=char)
                return render(
                    request, "wod/characters/mage/mage/4_powers.html", context,
                )
            form.assign()
            if (
                char.has_backgrounds()
                and char.has_affinity_sphere()
                and char.has_focus()
            ):
                char.next_stage()
                context["resonances"] = Resonance.objects.all().order_by("name")
                context["form"] = MagePowersForm(character=char)
                return render(
                    request, "wod/characters/mage/mage/4_powers.html", context,
                )
            context["form"] = MageAdvantagesForm(character=char)
            return render(
                request, "wod/characters/mage/mage/3_advantages.html", context,
            )
        if char.creation_status == 4:
            form = MagePowersForm(request.POST, character=char)
            if "Back" in form.data:
                char.prev_stage()
                context["form"] = MageAdvantagesForm(character=char)
                return render(
                    request, "wod/characters/mage/mage/3_advantages.html", context,
                )
            if "Random Powers" in form.data:
                char.random_spheres()
                char.random_resonance()
                char.next_stage()
                MFFormset = formset_factory(MeritFlawForm, extra=1)
                context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
                context["form"] = MageFreebieForm(character=char)
                return render(
                    request, "wod/characters/mage/mage/5_freebies.html", context,
                )
            form.assign()
            if char.has_spheres() and char.total_resonance() > 0:
                char.next_stage()
                MFFormset = formset_factory(MeritFlawForm, extra=1)
                context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
                context["form"] = MageFreebieForm(character=char)
                return render(
                    request, "wod/characters/mage/mage/5_freebies.html", context,
                )
            context["resonances"] = Resonance.objects.all().order_by("name")
            context["form"] = MagePowersForm(character=char)
            return render(request, "wod/characters/mage/mage/4_powers.html", context,)
        if char.creation_status == 5:
            form = MageFreebieForm(request.POST, character=char)
            if "Back" in form.data:
                char.prev_stage()
                context["resonances"] = Resonance.objects.all().order_by("name")
                context["form"] = MagePowersForm(character=char)
                return render(
                    request, "wod/characters/mage/mage/4_powers.html", context,
                )
            if "Random Freebies" in form.data:
                char.random_freebies()
                char.next_stage()
                context["form"] = MageDescriptionForm(character=char)
                return render(
                    request, "wod/characters/mage/mage/6_description.html", context,
                )
            form.full_clean()
            if form.total_cost_freebies() == char.freebies:
                form.assign()
                char.next_stage()
                context["form"] = MageDescriptionForm(character=char)
                return render(
                    request, "wod/characters/mage/mage/6_description.html", context,
                )
            MFFormset = formset_factory(MeritFlawForm, extra=1)
            context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
            context["form"] = MageFreebieForm(character=char)
            return render(request, "wod/characters/mage/mage/5_freebies.html", context,)
        if char.creation_status == 6:
            form = MageDescriptionForm(request.POST, character=char)
            if "Back" in form.data:
                char.prev_stage()
                MFFormset = formset_factory(MeritFlawForm, extra=1)
                context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
                context["form"] = MageFreebieForm(character=char)
                return render(
                    request, "wod/characters/mage/mage/5_freebies.html", context,
                )
            if "Random Description" in form.data:
                char.update_status("Sub")
                char.random_history()
                char.random_mage_history()
                char.random_finishing_touches()
                char.mf_based_corrections()
                char.next_stage()
                return render(request, "wod/characters/mage/mage/detail.html", context,)
            form.full_clean()
            if form.complete():
                for key, value in form.cleaned_data.items():
                    setattr(char, key, value)
                char.next_stage()
                return render(request, "wod/characters/mage/mage/detail.html", context,)
            context["form"] = MageDescriptionForm(character=char)
            return render(
                request, "wod/characters/mage/mage/6_description.html", context,
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

        context["resonance"] = ResRating.objects.filter(
            mage=mage, rating__gte=1
        ).order_by("resonance__name")
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
        context['scenes'] = Scene.objects.filter(characters=mage).order_by('date_of_scene')
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
