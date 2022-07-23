from django.views.generic import CreateView, DetailView, UpdateView

from wod.models.characters.human import (
    Archetype,
    Character,
    Group,
    Human,
    MeritFlaw,
    Specialty,
)


class CharacterDetailView(DetailView):
    model = Character
    template_name = "wod/characters/human/character/detail.html"


class CharacterCreateView(CreateView):
    model = Character
    fields = "__all__"
    template_name = "wod/characters/human/character/create.html"


class CharacterUpdateView(UpdateView):
    model = Character
    fields = "__all__"
    template_name = "wod/characters/human/character/update.html"


class HumanDetailView(DetailView):
    model = Human
    template_name = "wod/characters/human/human/detail.html"


class HumanCreateView(CreateView):
    model = Human
    fields = "__all__"
    template_name = "wod/characters/human/human/create.html"


class HumanUpdateView(UpdateView):
    model = Human
    fields = "__all__"
    template_name = "wod/characters/human/human/update.html"


class GroupDetailView(DetailView):
    model = Group
    template_name = "wod/characters/human/group/detail.html"


class GroupCreateView(CreateView):
    model = Group
    fields = "__all__"
    template_name = "wod/characters/human/group/create.html"


class GroupUpdateView(UpdateView):
    model = Group
    fields = "__all__"
    template_name = "wod/characters/human/group/update.html"


class ArchetypeDetailView(DetailView):
    model = Archetype
    template_name = "wod/characters/human/archetype/detail.html"


class ArchetypeCreateView(CreateView):
    model = Archetype
    fields = "__all__"
    template_name = "wod/characters/human/archetype/create.html"


class ArchetypeUpdateView(UpdateView):
    model = Archetype
    fields = "__all__"
    template_name = "wod/characters/human/archetype/update.html"


class MeritFlawDetailView(DetailView):
    model = MeritFlaw
    template_name = "wod/characters/human/meritflaw/detail.html"


class MeritFlawCreateView(CreateView):
    model = MeritFlaw
    fields = "__all__"
    template_name = "wod/characters/human/meritflaw/create.html"


class MeritFlawUpdateView(UpdateView):
    model = MeritFlaw
    fields = "__all__"
    template_name = "wod/characters/human/meritflaw/update.html"


class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = "wod/characters/human/specialty/detail.html"


class SpecialtyCreateView(CreateView):
    model = Specialty
    fields = "__all__"
    template_name = "wod/characters/human/specialty/create.html"


class SpecialtyUpdateView(UpdateView):
    model = Specialty
    fields = "__all__"
    template_name = "wod/characters/human/specialty/update.html"
