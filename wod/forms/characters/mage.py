from django import forms

from core.fields import ListTextWidget
from game.models.chronicle import Chronicle
from wod.models.characters.human import Archetype, MeritFlaw
from wod.models.characters.mage import Mage, MageFaction


class MageForm(forms.ModelForm):
    class Meta:
        model = Mage
        fields = "__all__"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["merits_and_flaws"].queryset = MeritFlaw.objects.filter(
            pk__in=[x.id for x in MeritFlaw.objects.all() if x.mage]
        )
        self.fields["affiliation"].queryset = MageFaction.objects.filter(parent=None)
        self.fields["faction"].queryset = MageFaction.objects.none()
        self.fields["subfaction"].queryset = MageFaction.objects.none()

        if "affiliation" in self.data:
            try:
                affiliation_id = int(self.data.get("affiliation"))
                self.fields["faction"] = MageFaction.objects.filter(
                    parent=affiliation_id
                )
            except (ValueError, TypeError):
                print("failed")
        if "faction" in self.data:
            try:
                faction_id = int(self.data.get("faction"))
                self.fields["subfaction"] = MageFaction.objects.filter(
                    parent=faction_id
                )
            except (ValueError, TypeError):
                pass


class ResonanceForm(forms.Form):
    char_field_with_list = forms.CharField(required=True)
    rating = forms.IntegerField(max_value=5, min_value=1, initial=1)

    def __init__(self, *args, **kwargs):
        _resonance_list = kwargs.pop("data_list", None)
        super().__init__(*args, **kwargs)
        # the "name" parameter will allow you to use the same widget more than once in the same
        # form, not setting this parameter differently will cause all inputs display the
        # same list.
        self.fields["char_field_with_list"].widget = ListTextWidget(
            data_list=_resonance_list, name="resonance-list"
        )


class MageCreationForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    concept = forms.CharField(label="Concept", max_length=100)
    chronicle = forms.ModelChoiceField(
        required=False,
        queryset=Chronicle.objects.all(),
        # TODO: Restrict to Chronicles allowing mages
        empty_label="----",
    )
    nature = forms.ModelChoiceField(queryset=Archetype.objects.all(), empty_label="----")
    demeanor = forms.ModelChoiceField(queryset=Archetype.objects.all(), empty_label="----")
    affiliation = forms.ModelChoiceField(queryset=MageFaction.objects.filter(parent=None), empty_label="----")
    essence = forms.CharField(widget=forms.Select(choices=[("----", "----"), ("Dynamic", "Dynamic"),
            ("Pattern", "Pattern"),
            ("Primordial", "Primordial"),
            ("Questing", "Questing"),]),)
    faction = forms.ModelChoiceField(queryset=MageFaction.objects.none(), empty_label="----")
    subfaction = forms.ModelChoiceField(queryset=MageFaction.objects.none(), empty_label="----")

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
    pass

class MageBackgroundsForm(forms.Form):
    pass

class MageSpheresForm(forms.Form):
    pass

class MageFocusForm(forms.Form):
    pass

class MageRotesForm(forms.Form):
    pass

class MageMeritsAndFlawsForm(forms.Form):
    pass

class MageResonanceForm(forms.Form):
    pass

class MageLanguagesForm(forms.Form):
    pass

class MageAppearanceForm(forms.Form):
    pass

class MageHistoryForm(forms.Form):
    pass
