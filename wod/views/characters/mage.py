from django.forms import formset_factory
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from core.models import Language
from core.views import BaseCharacterView
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
from wod.views.characters.human import AttributeDetailView


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
            affiliation = form.cleaned_data.get("affiliation")
            faction = form.cleaned_data.get("faction")
            subfaction = form.cleaned_data.get("subfaction")
            s = Mage.objects.create(
                name=form.data["name"],
                concept=form.data["concept"],
                demeanor=form.cleaned_data["demeanor"],
                nature=form.cleaned_data["nature"],
                owner=request.user,
                status="Un",
                chronicle=form.cleaned_data["chronicle"],
            )
            s.set_faction(affiliation, faction, subfaction=subfaction)
            return redirect(s.get_absolute_url())
        context = {}
        context["form"] = MageCreationForm()
        return render(request, "wod/characters/mage/mage/create.html", context)


class MageAbilitiesDetailView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        context["form"] = MageAbilitiesForm(character=character)
        return render(request, "wod/characters/mage/mage/2_abilities.html", context)

    def post(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        form = MageAbilitiesForm(request.POST, character=character)
        if "Back" in form.data:
            character.prev_stage()
            return redirect(character.get_absolute_url())
        if "Random Abilities" in form.data:
            character.random_abilities()
            character.next_stage()
            return redirect(character.get_absolute_url())
        form.assign()
        if character.has_abilities():
            character.next_stage()
            return redirect(character.get_absolute_url())
        context["form"] = MageAbilitiesForm(character=character)
        return redirect(character.get_absolute_url())


class MageAdvantagesView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        context["form"] = MageAdvantagesForm(character=character)
        return render(request, "wod/characters/mage/mage/3_advantages.html", context)

    def post(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        form = MageAdvantagesForm(request.POST, character=character)
        if "Back" in form.data:
            character.prev_stage()
            context["form"] = MageAbilitiesForm(character=character)
            return redirect(character.get_absolute_url())
        if "Random Advantages" in form.data:
            character.random_focus()
            character.random_backgrounds()
            character.random_arete()
            character.random_affinity_sphere()
            character.next_stage()
            context["resonances"] = Resonance.objects.all().order_by("name")
            context["form"] = MagePowersForm(character=character)
            return redirect(character.get_absolute_url())
        form.assign()
        if (
            character.has_backgrounds()
            and character.has_affinity_sphere()
            and character.has_focus()
        ):
            character.next_stage()
            context["resonances"] = Resonance.objects.all().order_by("name")
            context["form"] = MagePowersForm(character=character)
            return redirect(character.get_absolute_url())
        context["form"] = MageAdvantagesForm(character=character)
        return redirect(character.get_absolute_url())


class MagePowersView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        context["resonances"] = Resonance.objects.all().order_by("name")
        context["form"] = MagePowersForm(character=character)
        return render(request, "wod/characters/mage/mage/4_powers.html", context,)

    def post(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        form = MagePowersForm(request.POST, character=character)
        if "Back" in form.data:
            character.prev_stage()
            context["form"] = MageAdvantagesForm(character=character)
            return redirect(character.get_absolute_url())
        if "Random Powers" in form.data:
            character.random_spheres()
            character.random_resonance()
            character.next_stage()
            MFFormset = formset_factory(MeritFlawForm, extra=1)
            context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
            context["form"] = MageFreebieForm(character=character)
            return redirect(character.get_absolute_url())
        form.assign()
        if character.has_spheres() and character.total_resonance() > 0:
            character.next_stage()
            MFFormset = formset_factory(MeritFlawForm, extra=1)
            context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
            context["form"] = MageFreebieForm(character=character)
            return redirect(character.get_absolute_url())
        context["resonances"] = Resonance.objects.all().order_by("name")
        context["form"] = MagePowersForm(character=character)
        return redirect(character.get_absolute_url())


class MageFreebiesView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        MFFormset = formset_factory(MeritFlawForm, extra=1)
        context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
        context["form"] = MageFreebieForm(character=character)
        return render(request, "wod/characters/mage/mage/5_freebies.html", context)

    def post(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        form = MageFreebieForm(request.POST, character=character)
        if "Back" in form.data:
            character.prev_stage()
            context["resonances"] = Resonance.objects.all().order_by("name")
            context["form"] = MagePowersForm(character=character)
            return redirect(character.get_absolute_url())
        if "Random Freebies" in form.data:
            character.random_freebies()
            character.next_stage()
            context["form"] = MageDescriptionForm(character=character)
            return redirect(character.get_absolute_url())
        form.full_clean()
        if form.total_cost_freebies() == character.freebies:
            form.assign()
            character.next_stage()
            context["form"] = MageDescriptionForm(character=character)
            return redirect(character.get_absolute_url())
        MFFormset = formset_factory(MeritFlawForm, extra=1)
        context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
        context["form"] = MageFreebieForm(character=character)
        return redirect(character.get_absolute_url())


class MageDescriptionView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        context["form"] = MageDescriptionForm(character=character)
        return render(request, "wod/characters/mage/mage/6_description.html", context)

    def post(self, request, *args, **kwargs):
        character = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        form = MageDescriptionForm(request.POST, character=character)
        if "Back" in form.data:
            character.prev_stage()
            MFFormset = formset_factory(MeritFlawForm, extra=1)
            context["formset"] = MFFormset(form_kwargs={"chartype": "mage"})
            context["form"] = MageFreebieForm(character=character)
            return redirect(character.get_absolute_url())
        if "Random Description" in form.data:
            character.update_status("Sub")
            character.random_history()
            character.random_mage_history()
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
        context["form"] = MageDescriptionForm(character=character)
        return redirect(character.get_absolute_url())


class MageDetailView(BaseCharacterView):
    stage_views = {
        1: AttributeDetailView,
        2: MageAbilitiesDetailView,
        3: MageAdvantagesView,
        4: MagePowersView,
        5: MageFreebiesView,
        6: MageDescriptionView,
    }

    def get(self, request, *args, **kwargs):
        char = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)
        if char.status != "Un":
            return render(request, "wod/characters/mage/mage/detail.html", context,)
        if char.creation_status in self.stage_views.keys():
            return self.stage_views[char.creation_status].as_view()(
                request, *args, **kwargs
            )
        return render(request, "wod/characters/mage/mage/detail.html", context,)

    def post(self, request, *args, **kwargs):
        char = Mage.objects.get(pk=kwargs["pk"])
        context = self.get_context(char)
        if char.creation_status in self.stage_views.keys():
            return self.stage_views[char.creation_status].as_view()(
                request, *args, **kwargs
            )
        return render(request, "wod/characters/mage/mage/detail.html", context,)

    def get_context(self, character):
        context = super().get_context(character)
        context["resonance"] = ResRating.objects.filter(
            mage=character, rating__gte=1
        ).order_by("resonance__name")
        context["merits_and_flaws"] = MeritFlawRating.objects.order_by(
            "mf__name"
        ).filter(character=character)
        all_effects = list(Rote.objects.filter(mage=context["object"]))
        row_length = 2
        all_effects = [
            all_effects[i : i + row_length]
            for i in range(0, len(all_effects), row_length)
        ]
        context["rotes"] = all_effects
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
