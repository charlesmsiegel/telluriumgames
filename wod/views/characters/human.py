from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, View

from core.views import BaseCharacterView
from wod.forms.characters.human import AttributeForm
from wod.models.characters.human import (
    Archetype,
    Character,
    Derangement,
    Group,
    Human,
    MeritFlaw,
    WoDSpecialty,
)


class AttributeDetailView(BaseCharacterView):
    def get(self, request, *args, **kwargs):
        character = Human.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        context["form"] = AttributeForm(character=character)
        return render(request, "wod/characters/mage/mage/1_attribute.html", context)

    def post(self, request, *args, **kwargs):
        character = Human.objects.get(pk=kwargs["pk"])
        context = self.get_context(character)
        context["form"] = AttributeForm(character=character)
        form = AttributeForm(request.POST, character=character)
        if "Random Attributes" in form.data:
            character.random_attributes()
            character.next_stage()
            return redirect(character.get_absolute_url())
        form.assign()
        if character.has_attributes():
            character.next_stage()
            return redirect(character.get_absolute_url())
        context["form"] = AttributeForm(character=character)
        return redirect(character.get_absolute_url())


class CharacterDetailView(DetailView):
    model = Character
    template_name = "wod/characters/human/character/detail.html"


class CharacterCreateView(CreateView):
    model = Character
    fields = "__all__"
    template_name = "wod/characters/human/character/form.html"


class CharacterUpdateView(UpdateView):
    model = Character
    fields = "__all__"
    template_name = "wod/characters/human/character/form.html"


class HumanDetailView(DetailView):
    model = Human
    template_name = "wod/characters/human/human/detail.html"


class HumanCreateView(CreateView):
    model = Human
    fields = "__all__"
    template_name = "wod/characters/human/human/form.html"


class HumanUpdateView(UpdateView):
    model = Human
    fields = "__all__"
    template_name = "wod/characters/human/human/form.html"


class GroupDetailView(DetailView):
    model = Group
    template_name = "wod/characters/human/group/detail.html"


class GroupCreateView(CreateView):
    model = Group
    fields = "__all__"
    template_name = "wod/characters/human/group/form.html"


class GroupUpdateView(UpdateView):
    model = Group
    fields = "__all__"
    template_name = "wod/characters/human/group/form.html"


class ArchetypeDetailView(DetailView):
    model = Archetype
    template_name = "wod/characters/human/archetype/detail.html"


class ArchetypeCreateView(CreateView):
    model = Archetype
    fields = "__all__"
    template_name = "wod/characters/human/archetype/form.html"


class ArchetypeUpdateView(UpdateView):
    model = Archetype
    fields = ["name", "description"]
    template_name = "wod/characters/human/archetype/form.html"


class MeritFlawDetailView(View):
    def get(self, request, *args, **kwargs):
        mf = MeritFlaw.objects.get(pk=kwargs["pk"])
        context = self.get_context(mf)
        return render(request, "wod/characters/human/meritflaw/detail.html", context)

    def get_context(self, mf):
        context = {}
        context["object"] = mf
        context["ratings"] = ", ".join([str(x) for x in mf.ratings])
        return context


class MeritFlawCreateView(CreateView):
    model = MeritFlaw
    fields = "__all__"
    template_name = "wod/characters/human/meritflaw/form.html"


class MeritFlawUpdateView(UpdateView):
    model = MeritFlaw
    fields = ["name", "ratings", "human", "garou", "kinfolk", "mage", "description"]
    template_name = "wod/characters/human/meritflaw/form.html"


class SpecialtyDetailView(DetailView):
    model = WoDSpecialty
    template_name = "wod/characters/human/specialty/detail.html"


class SpecialtyCreateView(CreateView):
    model = WoDSpecialty
    fields = "__all__"
    template_name = "wod/characters/human/specialty/form.html"


class SpecialtyUpdateView(UpdateView):
    model = WoDSpecialty
    fields = "__all__"
    template_name = "wod/characters/human/specialty/form.html"


class DerangementDetailView(DetailView):
    model = Derangement
    template_name = "wod/characters/human/derangement/detail.html"


class DerangementCreateView(CreateView):
    model = Derangement
    fields = "__all__"
    template_name = "wod/characters/human/derangement/form.html"


class DerangementUpdateView(UpdateView):
    model = Derangement
    fields = "__all__"
    template_name = "wod/characters/human/derangement/form.html"
