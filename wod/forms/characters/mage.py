from django import forms

from core.models import Language
from game.models.chronicle import Chronicle
from wod.models.characters.human import Archetype, MeritFlaw
from wod.models.characters.mage import MageFaction
from wod.models.characters.mage.focus import Instrument, Paradigm, Practice
from wod.models.characters.mage.resonance import Resonance


class MageCreationForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    concept = forms.CharField(label="Concept", max_length=100)
    chronicle = forms.ModelChoiceField(
        required=False,
        queryset=Chronicle.objects.filter(
            allowed_objects__name="Mage", allowed_objects__system="wod"
        ),
    )
    nature = forms.ModelChoiceField(queryset=Archetype.objects.all())
    demeanor = forms.ModelChoiceField(queryset=Archetype.objects.all())
    affiliation = forms.ModelChoiceField(
        queryset=MageFaction.objects.filter(parent=None)
    )
    essence = forms.CharField(
        widget=forms.Select(
            choices=[
                ("---------", "---------"),
                ("Dynamic", "Dynamic"),
                ("Pattern", "Pattern"),
                ("Primordial", "Primordial"),
                ("Questing", "Questing"),
            ]
        ),
    )
    faction = forms.ModelChoiceField(queryset=MageFaction.objects.none())
    subfaction = forms.ModelChoiceField(queryset=MageFaction.objects.none())


class MageAttributeForm(forms.Form):
    strength = forms.IntegerField(max_value=5, min_value=1)
    dexterity = forms.IntegerField(max_value=5, min_value=1)
    stamina = forms.IntegerField(max_value=5, min_value=1)
    charisma = forms.IntegerField(max_value=5, min_value=1)
    manipulation = forms.IntegerField(max_value=5, min_value=1)
    appearance = forms.IntegerField(max_value=5, min_value=1)
    perception = forms.IntegerField(max_value=5, min_value=1)
    intelligence = forms.IntegerField(max_value=5, min_value=1)
    wits = forms.IntegerField(max_value=5, min_value=1)

    def total_physical(self):
        self.full_clean()
        return (
            self.cleaned_data["strength"]
            + self.cleaned_data["dexterity"]
            + self.cleaned_data["stamina"]
        )

    def total_social(self):
        self.full_clean()
        return (
            self.cleaned_data["charisma"]
            + self.cleaned_data["manipulation"]
            + self.cleaned_data["appearance"]
        )

    def total_mental(self):
        self.full_clean()
        return (
            self.cleaned_data["perception"]
            + self.cleaned_data["intelligence"]
            + self.cleaned_data["wits"]
        )

    def has_attributes(self):
        triple = [10, 8, 6]
        other_triple = [
            self.total_physical(),
            self.total_social(),
            self.total_mental(),
        ]
        triple.sort()
        other_triple.sort()
        return triple == other_triple


class MageAbilitiesForm(forms.Form):
    alertness = forms.IntegerField(max_value=3, min_value=0)
    athletics = forms.IntegerField(max_value=3, min_value=0)
    brawl = forms.IntegerField(max_value=3, min_value=0)
    empathy = forms.IntegerField(max_value=3, min_value=0)
    expression = forms.IntegerField(max_value=3, min_value=0)
    intimidation = forms.IntegerField(max_value=3, min_value=0)
    streetwise = forms.IntegerField(max_value=3, min_value=0)
    subterfuge = forms.IntegerField(max_value=3, min_value=0)

    crafts = forms.IntegerField(max_value=3, min_value=0)
    drive = forms.IntegerField(max_value=3, min_value=0)
    etiquette = forms.IntegerField(max_value=3, min_value=0)
    firearms = forms.IntegerField(max_value=3, min_value=0)
    melee = forms.IntegerField(max_value=3, min_value=0)
    stealth = forms.IntegerField(max_value=3, min_value=0)

    academics = forms.IntegerField(max_value=3, min_value=0)
    computer = forms.IntegerField(max_value=3, min_value=0)
    investigation = forms.IntegerField(max_value=3, min_value=0)
    medicine = forms.IntegerField(max_value=3, min_value=0)
    science = forms.IntegerField(max_value=3, min_value=0)
    awareness = forms.IntegerField(max_value=3, min_value=0)
    art = forms.IntegerField(max_value=3, min_value=0)
    leadership = forms.IntegerField(max_value=3, min_value=0)
    animal_kinship = forms.IntegerField(max_value=3, min_value=0)
    blatancy = forms.IntegerField(max_value=3, min_value=0)
    carousing = forms.IntegerField(max_value=3, min_value=0)
    do = forms.IntegerField(max_value=3, min_value=0)
    flying = forms.IntegerField(max_value=3, min_value=0)
    high_ritual = forms.IntegerField(max_value=3, min_value=0)
    lucid_dreaming = forms.IntegerField(max_value=3, min_value=0)
    search = forms.IntegerField(max_value=3, min_value=0)
    seduction = forms.IntegerField(max_value=3, min_value=0)
    martial_arts = forms.IntegerField(max_value=3, min_value=0)
    meditation = forms.IntegerField(max_value=3, min_value=0)
    research = forms.IntegerField(max_value=3, min_value=0)
    survival = forms.IntegerField(max_value=3, min_value=0)
    technology = forms.IntegerField(max_value=3, min_value=0)
    acrobatics = forms.IntegerField(max_value=3, min_value=0)
    archery = forms.IntegerField(max_value=3, min_value=0)
    biotech = forms.IntegerField(max_value=3, min_value=0)
    energy_weapons = forms.IntegerField(max_value=3, min_value=0)
    hypertech = forms.IntegerField(max_value=3, min_value=0)
    jetpack = forms.IntegerField(max_value=3, min_value=0)
    riding = forms.IntegerField(max_value=3, min_value=0)
    torture = forms.IntegerField(max_value=3, min_value=0)
    cosmology = forms.IntegerField(max_value=3, min_value=0)
    enigmas = forms.IntegerField(max_value=3, min_value=0)
    esoterica = forms.IntegerField(max_value=3, min_value=0)
    law = forms.IntegerField(max_value=3, min_value=0)
    occult = forms.IntegerField(max_value=3, min_value=0)
    politics = forms.IntegerField(max_value=3, min_value=0)
    area_knowledge = forms.IntegerField(max_value=3, min_value=0)
    belief_systems = forms.IntegerField(max_value=3, min_value=0)
    cryptography = forms.IntegerField(max_value=3, min_value=0)
    demolitions = forms.IntegerField(max_value=3, min_value=0)
    finance = forms.IntegerField(max_value=3, min_value=0)
    lore = forms.IntegerField(max_value=3, min_value=0)
    media = forms.IntegerField(max_value=3, min_value=0)
    pharmacopeia = forms.IntegerField(max_value=3, min_value=0)

    cooking = forms.IntegerField(max_value=3, min_value=0)
    diplomacy = forms.IntegerField(max_value=3, min_value=0)
    instruction = forms.IntegerField(max_value=3, min_value=0)
    intrigue = forms.IntegerField(max_value=3, min_value=0)
    intuition = forms.IntegerField(max_value=3, min_value=0)
    mimicry = forms.IntegerField(max_value=3, min_value=0)
    negotiation = forms.IntegerField(max_value=3, min_value=0)
    newspeak = forms.IntegerField(max_value=3, min_value=0)
    scan = forms.IntegerField(max_value=3, min_value=0)
    scrounging = forms.IntegerField(max_value=3, min_value=0)
    style = forms.IntegerField(max_value=3, min_value=0)
    blind_fighting = forms.IntegerField(max_value=3, min_value=0)
    climbing = forms.IntegerField(max_value=3, min_value=0)
    disguise = forms.IntegerField(max_value=3, min_value=0)
    elusion = forms.IntegerField(max_value=3, min_value=0)
    escapology = forms.IntegerField(max_value=3, min_value=0)
    fast_draw = forms.IntegerField(max_value=3, min_value=0)
    fast_talk = forms.IntegerField(max_value=3, min_value=0)
    fencing = forms.IntegerField(max_value=3, min_value=0)
    fortune_telling = forms.IntegerField(max_value=3, min_value=0)
    gambling = forms.IntegerField(max_value=3, min_value=0)
    gunsmith = forms.IntegerField(max_value=3, min_value=0)
    heavy_weapons = forms.IntegerField(max_value=3, min_value=0)
    hunting = forms.IntegerField(max_value=3, min_value=0)
    hypnotism = forms.IntegerField(max_value=3, min_value=0)
    jury_rigging = forms.IntegerField(max_value=3, min_value=0)
    microgravity_operations = forms.IntegerField(max_value=3, min_value=0)
    misdirection = forms.IntegerField(max_value=3, min_value=0)
    networking = forms.IntegerField(max_value=3, min_value=0)
    pilot = forms.IntegerField(max_value=3, min_value=0)
    psychology = forms.IntegerField(max_value=3, min_value=0)
    security = forms.IntegerField(max_value=3, min_value=0)
    speed_reading = forms.IntegerField(max_value=3, min_value=0)
    swimming = forms.IntegerField(max_value=3, min_value=0)
    conspiracy_theory = forms.IntegerField(max_value=3, min_value=0)
    chantry_politics = forms.IntegerField(max_value=3, min_value=0)
    covert_culture = forms.IntegerField(max_value=3, min_value=0)
    cultural_savvy = forms.IntegerField(max_value=3, min_value=0)
    helmsman = forms.IntegerField(max_value=3, min_value=0)
    history_knowledge = forms.IntegerField(max_value=3, min_value=0)
    power_brokering = forms.IntegerField(max_value=3, min_value=0)
    propaganda = forms.IntegerField(max_value=3, min_value=0)
    theology = forms.IntegerField(max_value=3, min_value=0)
    unconventional_warface = forms.IntegerField(max_value=3, min_value=0)
    vice = forms.IntegerField(max_value=3, min_value=0)

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")
        super().__init__(*args, **kwargs)

    def total_talents(self):
        self.full_clean()
        talent_list = self.char.get_talents().keys()
        if self.char.faction.name != "Akashayana":
            talent_list = [x for x in talent_list if x != "do"]
        return sum(self.cleaned_data[x] for x in talent_list)

    def total_skills(self):
        self.full_clean()
        skill_list = self.char.get_skills().keys()
        return sum(self.cleaned_data[x] for x in skill_list)

    def total_knowledges(self):
        self.full_clean()
        knowledge_list = self.char.get_knowledges().keys()
        return sum(self.cleaned_data[x] for x in knowledge_list)

    def has_abilities(self):
        triple = [13, 9, 5]
        other_triple = [
            self.total_talents(),
            self.total_skills(),
            self.total_knowledges(),
        ]
        triple.sort()
        other_triple.sort()
        return triple == other_triple


class MageAdvantagesForm(forms.Form):
    allies = forms.IntegerField(max_value=5, min_value=0)
    alternate_identity = forms.IntegerField(max_value=5, min_value=0)
    arcane = forms.IntegerField(max_value=5, min_value=0)
    avatar = forms.IntegerField(max_value=5, min_value=0)
    backup = forms.IntegerField(max_value=5, min_value=0)
    blessing = forms.IntegerField(max_value=5, min_value=0)
    certification = forms.IntegerField(max_value=5, min_value=0)
    chantry = forms.IntegerField(max_value=5, min_value=0)
    contacts = forms.IntegerField(max_value=5, min_value=0)
    cult = forms.IntegerField(max_value=5, min_value=0)
    demesne = forms.IntegerField(max_value=5, min_value=0)
    destiny = forms.IntegerField(max_value=5, min_value=0)
    dream = forms.IntegerField(max_value=5, min_value=0)
    enhancement = forms.IntegerField(max_value=5, min_value=0)
    fame = forms.IntegerField(max_value=5, min_value=0)
    familiar = forms.IntegerField(max_value=5, min_value=0)
    influence = forms.IntegerField(max_value=5, min_value=0)
    legend = forms.IntegerField(max_value=5, min_value=0)
    library = forms.IntegerField(max_value=5, min_value=0)
    mentor = forms.IntegerField(max_value=5, min_value=0)
    node = forms.IntegerField(max_value=5, min_value=0)
    past_lives = forms.IntegerField(max_value=5, min_value=0)
    patron = forms.IntegerField(max_value=5, min_value=0)
    rank = forms.IntegerField(max_value=5, min_value=0)
    requisitions = forms.IntegerField(max_value=5, min_value=0)
    resources = forms.IntegerField(max_value=5, min_value=0)
    retainers = forms.IntegerField(max_value=5, min_value=0)
    sanctum = forms.IntegerField(max_value=5, min_value=0)
    secret_weapons = forms.IntegerField(max_value=5, min_value=0)
    spies = forms.IntegerField(max_value=5, min_value=0)
    status_background = forms.IntegerField(max_value=5, min_value=0)
    totem = forms.IntegerField(max_value=5, min_value=0)
    wonder = forms.IntegerField(max_value=5, min_value=0)

    arete = forms.IntegerField(max_value=3, min_value=1)

    affinity_sphere = forms.CharField(widget=forms.Select(choices=[("----", "----")]),)

    paradigms = forms.ModelMultipleChoiceField(
        required=False, queryset=Paradigm.objects.all()
    )
    practices = forms.ModelMultipleChoiceField(
        required=False, queryset=Practice.objects.all()
    )
    instruments = forms.ModelMultipleChoiceField(
        required=False, queryset=Instrument.objects.all()
    )
    # TODO: Improve querysets for easier creation

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")
        choices = [
            (x, x.title())
            for x in self.char.faction.affinities + self.char.subfaction.affinities
        ]
        choices = list(set(choices))
        # TODO: When replacing JSONs, this will become ModelChoiceField
        choices.sort()
        super().__init__(*args, **kwargs)
        self.fields["affinity_sphere"].widget.choices += choices

    def has_backgrounds(self):
        self.full_clean()
        backgrounds = self.char.get_backgrounds().keys()
        total_backgrounds = sum(self.cleaned_data[x] for x in backgrounds)
        total_backgrounds += self.cleaned_data["totem"]
        total_backgrounds += self.cleaned_data["enhancement"]
        total_backgrounds += self.cleaned_data["sanctum"]
        return total_backgrounds == 7

    def has_affinity_sphere(self):
        self.full_clean()
        return self.cleaned_data["affinity_sphere"] != "----"

    def has_focus(self):
        paradigms = self.cleaned_data["paradigms"].count() >= 1
        practices = self.cleaned_data["practices"].count() >= 1
        instruments = self.cleaned_data["paradigms"].count() >= 7
        return paradigms + practices + instruments

    def complete(self):
        return (
            self.has_backgrounds() and self.has_affinity_sphere() and self.has_focus()
        )


class MagePowersForm(forms.Form):
    correspondence = forms.IntegerField(max_value=5, min_value=0)
    time = forms.IntegerField(max_value=5, min_value=0)
    spirit = forms.IntegerField(max_value=5, min_value=0)
    mind = forms.IntegerField(max_value=5, min_value=0)
    entropy = forms.IntegerField(max_value=5, min_value=0)
    prime = forms.IntegerField(max_value=5, min_value=0)
    forces = forms.IntegerField(max_value=5, min_value=0)
    matter = forms.IntegerField(max_value=5, min_value=0)
    life = forms.IntegerField(max_value=5, min_value=0)

    resonance = forms.ModelChoiceField(
        queryset=Resonance.objects.all().order_by("name")
    )
    # TODO: Upgrade to input + pulldown box

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")
        super().__init__(*args, **kwargs)
        for sphere in [
            "correspondence",
            "time",
            "spirit",
            "mind",
            "entropy",
            "prime",
            "forces",
            "matter",
            "life",
        ]:
            self.fields[sphere] = forms.IntegerField(
                max_value=self.char.arete, min_value=0
            )
        self.fields[self.char.affinity_sphere] = self.fields[
            sphere
        ] = forms.IntegerField(max_value=self.char.arete, min_value=1)

    def complete(self):
        self.full_clean()
        return sum(self.cleaned_data[x] for x in self.char.get_spheres().keys()) == 6


class MageMeritFlawForm(forms.Form):
    mf = forms.ModelChoiceField(queryset=MeritFlaw.objects.filter(mage=True))
    rating = forms.ChoiceField(choices=[("---", "---")])


class MageFreebieForm(forms.Form):
    strength = forms.IntegerField(max_value=5, min_value=1)
    dexterity = forms.IntegerField(max_value=5, min_value=1)
    stamina = forms.IntegerField(max_value=5, min_value=1)
    charisma = forms.IntegerField(max_value=5, min_value=1)
    manipulation = forms.IntegerField(max_value=5, min_value=1)
    appearance = forms.IntegerField(max_value=5, min_value=1)
    perception = forms.IntegerField(max_value=5, min_value=1)
    intelligence = forms.IntegerField(max_value=5, min_value=1)
    wits = forms.IntegerField(max_value=5, min_value=1)
    alertness = forms.IntegerField(max_value=3, min_value=0)
    athletics = forms.IntegerField(max_value=3, min_value=0)
    brawl = forms.IntegerField(max_value=3, min_value=0)
    empathy = forms.IntegerField(max_value=3, min_value=0)
    expression = forms.IntegerField(max_value=3, min_value=0)
    intimidation = forms.IntegerField(max_value=3, min_value=0)
    streetwise = forms.IntegerField(max_value=3, min_value=0)
    subterfuge = forms.IntegerField(max_value=3, min_value=0)

    crafts = forms.IntegerField(max_value=3, min_value=0)
    drive = forms.IntegerField(max_value=3, min_value=0)
    etiquette = forms.IntegerField(max_value=3, min_value=0)
    firearms = forms.IntegerField(max_value=3, min_value=0)
    melee = forms.IntegerField(max_value=3, min_value=0)
    stealth = forms.IntegerField(max_value=3, min_value=0)

    academics = forms.IntegerField(max_value=3, min_value=0)
    computer = forms.IntegerField(max_value=3, min_value=0)
    investigation = forms.IntegerField(max_value=3, min_value=0)
    medicine = forms.IntegerField(max_value=3, min_value=0)
    science = forms.IntegerField(max_value=3, min_value=0)
    awareness = forms.IntegerField(max_value=3, min_value=0)
    art = forms.IntegerField(max_value=3, min_value=0)
    leadership = forms.IntegerField(max_value=3, min_value=0)
    animal_kinship = forms.IntegerField(max_value=3, min_value=0)
    blatancy = forms.IntegerField(max_value=3, min_value=0)
    carousing = forms.IntegerField(max_value=3, min_value=0)
    do = forms.IntegerField(max_value=3, min_value=0)
    flying = forms.IntegerField(max_value=3, min_value=0)
    high_ritual = forms.IntegerField(max_value=3, min_value=0)
    lucid_dreaming = forms.IntegerField(max_value=3, min_value=0)
    search = forms.IntegerField(max_value=3, min_value=0)
    seduction = forms.IntegerField(max_value=3, min_value=0)
    martial_arts = forms.IntegerField(max_value=3, min_value=0)
    meditation = forms.IntegerField(max_value=3, min_value=0)
    research = forms.IntegerField(max_value=3, min_value=0)
    survival = forms.IntegerField(max_value=3, min_value=0)
    technology = forms.IntegerField(max_value=3, min_value=0)
    acrobatics = forms.IntegerField(max_value=3, min_value=0)
    archery = forms.IntegerField(max_value=3, min_value=0)
    biotech = forms.IntegerField(max_value=3, min_value=0)
    energy_weapons = forms.IntegerField(max_value=3, min_value=0)
    hypertech = forms.IntegerField(max_value=3, min_value=0)
    jetpack = forms.IntegerField(max_value=3, min_value=0)
    riding = forms.IntegerField(max_value=3, min_value=0)
    torture = forms.IntegerField(max_value=3, min_value=0)
    cosmology = forms.IntegerField(max_value=3, min_value=0)
    enigmas = forms.IntegerField(max_value=3, min_value=0)
    esoterica = forms.IntegerField(max_value=3, min_value=0)
    law = forms.IntegerField(max_value=3, min_value=0)
    occult = forms.IntegerField(max_value=3, min_value=0)
    politics = forms.IntegerField(max_value=3, min_value=0)
    area_knowledge = forms.IntegerField(max_value=3, min_value=0)
    belief_systems = forms.IntegerField(max_value=3, min_value=0)
    cryptography = forms.IntegerField(max_value=3, min_value=0)
    demolitions = forms.IntegerField(max_value=3, min_value=0)
    finance = forms.IntegerField(max_value=3, min_value=0)
    lore = forms.IntegerField(max_value=3, min_value=0)
    media = forms.IntegerField(max_value=3, min_value=0)
    pharmacopeia = forms.IntegerField(max_value=3, min_value=0)

    cooking = forms.IntegerField(max_value=3, min_value=0)
    diplomacy = forms.IntegerField(max_value=3, min_value=0)
    instruction = forms.IntegerField(max_value=3, min_value=0)
    intrigue = forms.IntegerField(max_value=3, min_value=0)
    intuition = forms.IntegerField(max_value=3, min_value=0)
    mimicry = forms.IntegerField(max_value=3, min_value=0)
    negotiation = forms.IntegerField(max_value=3, min_value=0)
    newspeak = forms.IntegerField(max_value=3, min_value=0)
    scan = forms.IntegerField(max_value=3, min_value=0)
    scrounging = forms.IntegerField(max_value=3, min_value=0)
    style = forms.IntegerField(max_value=3, min_value=0)
    blind_fighting = forms.IntegerField(max_value=3, min_value=0)
    climbing = forms.IntegerField(max_value=3, min_value=0)
    disguise = forms.IntegerField(max_value=3, min_value=0)
    elusion = forms.IntegerField(max_value=3, min_value=0)
    escapology = forms.IntegerField(max_value=3, min_value=0)
    fast_draw = forms.IntegerField(max_value=3, min_value=0)
    fast_talk = forms.IntegerField(max_value=3, min_value=0)
    fencing = forms.IntegerField(max_value=3, min_value=0)
    fortune_telling = forms.IntegerField(max_value=3, min_value=0)
    gambling = forms.IntegerField(max_value=3, min_value=0)
    gunsmith = forms.IntegerField(max_value=3, min_value=0)
    heavy_weapons = forms.IntegerField(max_value=3, min_value=0)
    hunting = forms.IntegerField(max_value=3, min_value=0)
    hypnotism = forms.IntegerField(max_value=3, min_value=0)
    jury_rigging = forms.IntegerField(max_value=3, min_value=0)
    microgravity_operations = forms.IntegerField(max_value=3, min_value=0)
    misdirection = forms.IntegerField(max_value=3, min_value=0)
    networking = forms.IntegerField(max_value=3, min_value=0)
    pilot = forms.IntegerField(max_value=3, min_value=0)
    psychology = forms.IntegerField(max_value=3, min_value=0)
    security = forms.IntegerField(max_value=3, min_value=0)
    speed_reading = forms.IntegerField(max_value=3, min_value=0)
    swimming = forms.IntegerField(max_value=3, min_value=0)
    conspiracy_theory = forms.IntegerField(max_value=3, min_value=0)
    chantry_politics = forms.IntegerField(max_value=3, min_value=0)
    covert_culture = forms.IntegerField(max_value=3, min_value=0)
    cultural_savvy = forms.IntegerField(max_value=3, min_value=0)
    helmsman = forms.IntegerField(max_value=3, min_value=0)
    history_knowledge = forms.IntegerField(max_value=3, min_value=0)
    power_brokering = forms.IntegerField(max_value=3, min_value=0)
    propaganda = forms.IntegerField(max_value=3, min_value=0)
    theology = forms.IntegerField(max_value=3, min_value=0)
    unconventional_warface = forms.IntegerField(max_value=3, min_value=0)
    vice = forms.IntegerField(max_value=3, min_value=0)
    allies = forms.IntegerField(max_value=5, min_value=0)
    alternate_identity = forms.IntegerField(max_value=5, min_value=0)
    arcane = forms.IntegerField(max_value=5, min_value=0)
    avatar = forms.IntegerField(max_value=5, min_value=0)
    backup = forms.IntegerField(max_value=5, min_value=0)
    blessing = forms.IntegerField(max_value=5, min_value=0)
    certification = forms.IntegerField(max_value=5, min_value=0)
    chantry = forms.IntegerField(max_value=5, min_value=0)
    contacts = forms.IntegerField(max_value=5, min_value=0)
    cult = forms.IntegerField(max_value=5, min_value=0)
    demesne = forms.IntegerField(max_value=5, min_value=0)
    destiny = forms.IntegerField(max_value=5, min_value=0)
    dream = forms.IntegerField(max_value=5, min_value=0)
    enhancement = forms.IntegerField(max_value=5, min_value=0)
    fame = forms.IntegerField(max_value=5, min_value=0)
    familiar = forms.IntegerField(max_value=5, min_value=0)
    influence = forms.IntegerField(max_value=5, min_value=0)
    legend = forms.IntegerField(max_value=5, min_value=0)
    library = forms.IntegerField(max_value=5, min_value=0)
    mentor = forms.IntegerField(max_value=5, min_value=0)
    node = forms.IntegerField(max_value=5, min_value=0)
    past_lives = forms.IntegerField(max_value=5, min_value=0)
    patron = forms.IntegerField(max_value=5, min_value=0)
    rank = forms.IntegerField(max_value=5, min_value=0)
    requisitions = forms.IntegerField(max_value=5, min_value=0)
    resources = forms.IntegerField(max_value=5, min_value=0)
    retainers = forms.IntegerField(max_value=5, min_value=0)
    sanctum = forms.IntegerField(max_value=5, min_value=0)
    secret_weapons = forms.IntegerField(max_value=5, min_value=0)
    spies = forms.IntegerField(max_value=5, min_value=0)
    status_background = forms.IntegerField(max_value=5, min_value=0)
    totem = forms.IntegerField(max_value=5, min_value=0)
    wonder = forms.IntegerField(max_value=5, min_value=0)

    arete = forms.IntegerField(max_value=3, min_value=1)

    correspondence = forms.IntegerField(max_value=5, min_value=0)
    time = forms.IntegerField(max_value=5, min_value=0)
    spirit = forms.IntegerField(max_value=5, min_value=0)
    mind = forms.IntegerField(max_value=5, min_value=0)
    entropy = forms.IntegerField(max_value=5, min_value=0)
    prime = forms.IntegerField(max_value=5, min_value=0)
    forces = forms.IntegerField(max_value=5, min_value=0)
    matter = forms.IntegerField(max_value=5, min_value=0)
    life = forms.IntegerField(max_value=5, min_value=0)

    willpower = forms.IntegerField(max_value=10, min_value=5)

    native_language = forms.ModelChoiceField(queryset=Language.objects.all())
    languages = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(), required=False
    )

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")
        super().__init__(*args, **kwargs)
        for sphere in self.char.get_spheres().keys():
            self.fields[sphere] = forms.IntegerField(
                max_value=self.char.arete, min_value=getattr(self.char, sphere)
            )
        for attribute in self.char.get_attributes().keys():
            self.fields[attribute] = forms.IntegerField(
                max_value=5, min_value=getattr(self.char, attribute)
            )
        for ability in self.char.get_abilities().keys():
            self.fields[ability] = forms.IntegerField(
                max_value=5, min_value=getattr(self.char, ability)
            )
        for bg in self.char.get_backgrounds().keys():
            self.fields[bg] = forms.IntegerField(
                max_value=5, min_value=getattr(self.char, bg)
            )
        self.fields["arete"] = forms.IntegerField(
            max_value=3, min_value=self.char.arete
        )

    def complete(self):
        self.full_clean()
        total = 0
        attr_total = 0
        for key, value in self.char.get_attributes().items():
            attr_total += self.cleaned_data[key] - value
        total += 5 * attr_total
        abb_total = 0
        for key, value in self.char.get_abilities().items():
            if self.char.faction.name == "Akashayana" or key != "do":
                abb_total += self.cleaned_data[key] - value
        total += 2 * abb_total
        total += 4 * (self.char.arete - 1)
        sphere_total = 0
        for key, value in self.char.get_spheres().items():
            sphere_total += self.cleaned_data[key] - value
        total += 7 * sphere_total
        bg_total = 0
        for key, value in self.char.get_backgrounds().items():
            bg_total += self.cleaned_data[key] - value
            if key in ["totem", "enhancement", "sanctum"]:
                bg_total += self.cleaned_data[key] - value
        total += 1 * bg_total
        total += self.cleaned_data["willpower"] - 5
        mf_keys = [
            x
            for x in self.data.keys()
            if x.startswith("form-") and (x.endswith("-mf") or x.endswith("-rating"))
        ]
        mf_values = [int(self.data[x]) for x in mf_keys]
        mfs = {k: v for k, v in zip(mf_keys, mf_values)}
        values = [mfs[k] for k in mfs.keys() if "-rating" in k]
        flaw_total = sum(x for x in values if x < 0)
        merit_total = sum(x for x in values if x > 0)
        if flaw_total < -7:
            return False
        total += merit_total
        total += flaw_total
        total += self.cleaned_data["languages"].count()
        return total == self.char.freebies


class MageDescriptionForm(forms.Form):
    age_of_awakening = forms.IntegerField(required=True)
    age = forms.IntegerField(required=True)
    apparent_age = forms.IntegerField(required=True)
    date_of_birth = forms.DateField(widget=forms.DateInput(), required=True)
    hair = forms.CharField(required=True)
    eyes = forms.CharField(required=True)
    ethnicity = forms.CharField(required=True)
    nationality = forms.CharField(required=True)
    height = forms.CharField(required=True)
    weight = forms.CharField(required=True)
    sex = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)

    childhood = forms.CharField(widget=forms.Textarea, required=True)
    history = forms.CharField(widget=forms.Textarea, required=True)
    goals = forms.CharField(widget=forms.Textarea, required=True)
    notes = forms.CharField(widget=forms.Textarea, required=True)

    awakening = forms.CharField(widget=forms.Textarea, required=True)
    seekings = forms.CharField(widget=forms.Textarea, required=True)
    quiets = forms.CharField(widget=forms.Textarea, required=True)
    avatar_description = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")
        super().__init__(*args, **kwargs)
