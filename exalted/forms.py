from django import forms

from exalted.models.characters.utils import ABILITIES


class RandomCharacterForm(forms.Form):
    character_type = forms.ChoiceField(
        choices=[("mortal", "Mortal"), ("solar", "Solar")]
    )
    name = forms.CharField(max_length=100, label="Name", required=False)
    xp = forms.IntegerField(initial=0, label="XP")

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["character_type"].choices = []


class ExMortalCreationForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    concept = forms.CharField(label="Name", max_length=100)
    # Native Language
    # Chronicle


class SolarCreationForm(ExMortalCreationForm):
    CASTE_CHOICES = ["dawn", "zenith", "twilight", "eclipse", "night"]
    caste = forms.CharField(
        label="Caste",
        widget=forms.Select(
            choices=zip(CASTE_CHOICES, [x.title() for x in CASTE_CHOICES])
        ),
    )
    # Anima


class ExaltedAttributeForm(forms.Form):
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
        triple = [11, 9, 7]
        other_triple = [
            self.total_physical(),
            self.total_social(),
            self.total_mental(),
        ]
        triple.sort()
        other_triple.sort()
        return triple == other_triple


class ExaltedAbilitiesForm(forms.Form):
    archery_check = forms.BooleanField(required=False)
    archery = forms.IntegerField(max_value=5, min_value=0)
    athletics_check = forms.BooleanField(required=False)
    athletics = forms.IntegerField(max_value=5, min_value=0)
    awareness_check = forms.BooleanField(required=False)
    awareness = forms.IntegerField(max_value=5, min_value=0)
    brawl_check = forms.BooleanField(required=False)
    brawl = forms.IntegerField(max_value=5, min_value=0)
    bureaucracy_check = forms.BooleanField(required=False)
    bureaucracy = forms.IntegerField(max_value=5, min_value=0)
    craft_check = forms.BooleanField(required=False)
    craft = forms.IntegerField(max_value=5, min_value=0)
    dodge_check = forms.BooleanField(required=False)
    dodge = forms.IntegerField(max_value=5, min_value=0)
    integrity_check = forms.BooleanField(required=False)
    integrity = forms.IntegerField(max_value=5, min_value=0)
    investigation_check = forms.BooleanField(required=False)
    investigation = forms.IntegerField(max_value=5, min_value=0)
    larceny_check = forms.BooleanField(required=False)
    larceny = forms.IntegerField(max_value=5, min_value=0)
    linguistics_check = forms.BooleanField(required=False)
    linguistics = forms.IntegerField(max_value=5, min_value=0)
    lore_check = forms.BooleanField(required=False)
    lore = forms.IntegerField(max_value=5, min_value=0)
    martial_arts_check = forms.BooleanField(required=False)
    martial_arts = forms.IntegerField(max_value=5, min_value=0)
    medicine_check = forms.BooleanField(required=False)
    medicine = forms.IntegerField(max_value=5, min_value=0)
    melee_check = forms.BooleanField(required=False)
    melee = forms.IntegerField(max_value=5, min_value=0)
    occult_check = forms.BooleanField(required=False)
    occult = forms.IntegerField(max_value=5, min_value=0)
    performance_check = forms.BooleanField(required=False)
    performance = forms.IntegerField(max_value=5, min_value=0)
    presence_check = forms.BooleanField(required=False)
    presence = forms.IntegerField(max_value=5, min_value=0)
    resistance_check = forms.BooleanField(required=False)
    resistance = forms.IntegerField(max_value=5, min_value=0)
    ride_check = forms.BooleanField(required=False)
    ride = forms.IntegerField(max_value=5, min_value=0)
    sail_check = forms.BooleanField(required=False)
    sail = forms.IntegerField(max_value=5, min_value=0)
    socialize_check = forms.BooleanField(required=False)
    socialize = forms.IntegerField(max_value=5, min_value=0)
    stealth_check = forms.BooleanField(required=False)
    stealth = forms.IntegerField(max_value=5, min_value=0)
    survival_check = forms.BooleanField(required=False)
    survival = forms.IntegerField(max_value=5, min_value=0)
    thrown_check = forms.BooleanField(required=False)
    thrown = forms.IntegerField(max_value=5, min_value=0)
    war_check = forms.BooleanField(required=False)
    war = forms.IntegerField(max_value=5, min_value=0)

    supernal_ability = forms.CharField(
        label="Supernal Ability", widget=forms.Select(choices=[]),
    )

    spec_1_ability = forms.CharField(
        widget=forms.Select(
            choices=[(x, x.replace("_", " ").title()) for x in ABILITIES]
        ),
    )
    spec_1_value = forms.CharField(max_length=50)
    spec_2_ability = forms.CharField(
        widget=forms.Select(
            choices=[(x, x.replace("_", " ").title()) for x in ABILITIES]
        ),
    )
    spec_2_value = forms.CharField(max_length=50)
    spec_3_ability = forms.CharField(
        widget=forms.Select(
            choices=[(x, x.replace("_", " ").title()) for x in ABILITIES]
        ),
    )
    spec_3_value = forms.CharField(max_length=50)
    spec_4_ability = forms.CharField(
        widget=forms.Select(
            choices=[(x, x.replace("_", " ").title()) for x in ABILITIES]
        ),
    )
    spec_4_value = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        char = kwargs.pop("character")
        ability_list = char.caste_ability_dict[char.caste]
        choices = [(x, x.replace("_", " ").title()) for x in ability_list]
        choices.sort(key=lambda x: x[0])
        super().__init__(*args, **kwargs)
        self.fields["supernal_ability"].widget.choices = choices

    def has_abilities(self, character):
        self.full_clean()
        all_dots = sum(self.cleaned_data[x] for x in ABILITIES) == 28
        checked_abilities = [
            x for x in ABILITIES if self.cleaned_data[x + "_check"] == True
        ]
        favored = len(checked_abilities) == 10
        caste_abilities = [
            x
            for x in checked_abilities
            if x in character.caste_ability_dict[character.caste]
        ]
        caste = len(caste_abilities) >= 5
        min_values = all([self.cleaned_data[x] > 0 for x in checked_abilities])
        supernal = self.cleaned_data["supernal_ability"] in checked_abilities
        specialties = (
            self.cleaned_data["spec_1_value"]
            and self.cleaned_data["spec_2_value"]
            and self.cleaned_data["spec_3_value"]
            and self.cleaned_data["spec_4_value"]
            and getattr(character, self.cleaned_data["spec_1_ability"]) > 0
            and getattr(character, self.cleaned_data["spec_2_ability"]) > 0
            and getattr(character, self.cleaned_data["spec_3_ability"]) > 0
            and getattr(character, self.cleaned_data["spec_4_ability"]) > 0
        )
        return (
            all_dots and favored and caste and specialties and supernal and min_values
        )
