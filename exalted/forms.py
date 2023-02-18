from django import forms

from exalted.models.characters.mortals import ExMerit
from exalted.models.characters.utils import ABILITIES
from game.models import Chronicle


class RandomCharacterForm(forms.Form):
    character_type = forms.ChoiceField(
        choices=[
            ("mortal", "Mortal"),
            ("solar", "Solar"),
            ("dragonblooded", "Dragon-Blooded"),
        ]
    )
    name = forms.CharField(max_length=100, label="Name", required=False)
    bonus = forms.IntegerField(initial=0, label="Bonus Points")
    xp = forms.IntegerField(initial=0, label="XP")


class ExMortalCreationForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    concept = forms.CharField(label="Name", max_length=100)
    # Native Language
    chronicle = forms.CharField(
        required=False,
        label="Chronicle",
        widget=forms.Select(choices=[(None, "----")]),
    )

    def __init__(self, *args, **kwargs):
        choices = [(x.name, x.name) for x in Chronicle.objects.all()]
        super().__init__(*args, **kwargs)
        self.fields["chronicle"].widget.choices += choices


class SolarCreationForm(ExMortalCreationForm):
    CASTE_CHOICES = ["dawn", "zenith", "twilight", "eclipse", "night"]
    caste = forms.CharField(
        label="Caste",
        widget=forms.Select(
            choices=zip(CASTE_CHOICES, [x.title() for x in CASTE_CHOICES])
        ),
    )
    anima = forms.CharField(max_length=100)


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
        checked_abilities = [x for x in ABILITIES if self.cleaned_data[x + "_check"]]
        favored = len(checked_abilities) == 10
        caste_abilities = [
            x
            for x in checked_abilities
            if x in character.caste_ability_dict[character.caste]
        ]
        caste = len(caste_abilities) >= 5
        max_values = all(self.cleaned_data[x] <= 3 for x in ABILITIES)
        min_values = all(self.cleaned_data[x] > 0 for x in checked_abilities)
        supernal = self.cleaned_data["supernal_ability"] in checked_abilities
        specialties = (
            self.cleaned_data["spec_1_value"]
            and self.cleaned_data["spec_2_value"]
            and self.cleaned_data["spec_3_value"]
            and self.cleaned_data["spec_4_value"]
            and self.cleaned_data[self.cleaned_data["spec_1_ability"]] > 0
            and self.cleaned_data[self.cleaned_data["spec_2_ability"]] > 0
            and self.cleaned_data[self.cleaned_data["spec_3_ability"]] > 0
            and self.cleaned_data[self.cleaned_data["spec_4_ability"]] > 0
        )
        if not all_dots:
            print("num_dots:", sum(self.cleaned_data[x] for x in ABILITIES))
        if not favored:
            print("favored:", len(checked_abilities))
        if not caste:
            print("caste:", len(caste_abilities))
        if not specialties:
            print(
                "specialty:",
                self.cleaned_data["spec_1_value"],
                self.cleaned_data["spec_2_value"],
                self.cleaned_data["spec_3_value"],
                self.cleaned_data["spec_4_value"],
                getattr(character, self.cleaned_data["spec_1_ability"]) > 0,
                getattr(character, self.cleaned_data["spec_2_ability"]) > 0,
                getattr(character, self.cleaned_data["spec_3_ability"]) > 0,
                getattr(character, self.cleaned_data["spec_4_ability"]) > 0,
            )
        if not supernal:
            print("supernal:", self.cleaned_data["supernal_ability"], checked_abilities)
        if not min_values:
            print(
                "min_values:",
                [
                    x
                    for x in zip(
                        checked_abilities,
                        [self.cleaned_data[x] for x in checked_abilities],
                    )
                    if x[1] == 0
                ],
            )
        if not max_values:
            print(
                "min_values:",
                [
                    x
                    for x in zip(ABILITIES, [self.cleaned_data[x] for x in ABILITIES])
                    if x[1] >= 4
                ],
            )
        return (
            all_dots
            and favored
            and caste
            and specialties
            and supernal
            and min_values
            and max_values
        )


class ExaltedMeritsForm(forms.Form):
    merit_1 = forms.CharField(widget=forms.Select(choices=[("----", "----")]),)
    merit_2 = forms.CharField(widget=forms.Select(choices=[("----", "----")]),)
    merit_3 = forms.CharField(widget=forms.Select(choices=[("----", "----")]),)
    merit_4 = forms.CharField(widget=forms.Select(choices=[("----", "----")]),)
    merit_5 = forms.CharField(widget=forms.Select(choices=[("----", "----")]),)
    merit_6 = forms.CharField(widget=forms.Select(choices=[("----", "----")]),)
    merit_7 = forms.CharField(widget=forms.Select(choices=[("----", "----")]),)
    merit_8 = forms.CharField(widget=forms.Select(choices=[("----", "----")]),)
    merit_9 = forms.CharField(widget=forms.Select(choices=[("----", "----")]),)
    merit_10 = forms.CharField(widget=forms.Select(choices=[("----", "----")]),)
    merit_1_rating = forms.IntegerField(widget=forms.Select(choices=[(0, 0)]))
    merit_2_rating = forms.IntegerField(widget=forms.Select(choices=[(0, 0)]))
    merit_3_rating = forms.IntegerField(widget=forms.Select(choices=[(0, 0)]))
    merit_4_rating = forms.IntegerField(widget=forms.Select(choices=[(0, 0)]))
    merit_5_rating = forms.IntegerField(widget=forms.Select(choices=[(0, 0)]))
    merit_6_rating = forms.IntegerField(widget=forms.Select(choices=[(0, 0)]))
    merit_7_rating = forms.IntegerField(widget=forms.Select(choices=[(0, 0)]))
    merit_8_rating = forms.IntegerField(widget=forms.Select(choices=[(0, 0)]))
    merit_9_rating = forms.IntegerField(widget=forms.Select(choices=[(0, 0)]))
    merit_10_rating = forms.IntegerField(widget=forms.Select(choices=[(0, 0)]))

    def __init__(self, *args, **kwargs):
        choices = [(x.name, x.name) for x in ExMerit.objects.all()]
        super().__init__(*args, **kwargs)
        self.fields["merit_1"].widget.choices += choices
        self.fields["merit_2"].widget.choices += choices
        self.fields["merit_3"].widget.choices += choices
        self.fields["merit_4"].widget.choices += choices
        self.fields["merit_5"].widget.choices += choices
        self.fields["merit_6"].widget.choices += choices
        self.fields["merit_7"].widget.choices += choices
        self.fields["merit_8"].widget.choices += choices
        self.fields["merit_9"].widget.choices += choices
        self.fields["merit_10"].widget.choices += choices

    def has_merits(self, character):
        self.full_clean()
        total = character.total_merits()
        merits = [self.cleaned_data[f"merit_{i}"] for i in range(1, 11)]
        merit_ratings = [self.cleaned_data[f"merit_{i}_rating"] for i in range(1, 11)]
        pairs = list(zip(merits, merit_ratings))
        pairs = [x for x in pairs if x[0] != "----"]
        pairs = [(ExMerit.objects.get(name=x[0]), x[1]) for x in pairs]
        pairs = [(x[0], x[1]) for x in pairs if x[1] in x[0].ratings]
        new_total = total + sum(x[1] for x in pairs)
        return new_total == 10


class ExaltedCharmForm(forms.Form):
    charm = forms.CharField(widget=forms.Select(choices=[]),)

    def __init__(self, *args, **kwargs):
        char = kwargs.pop("character")
        super().__init__(*args, **kwargs)
        self.fields["charm"].widget.choices = [
            (x.name, f"{x.name} ({x.statistic.replace('_', ' ').title()})")
            for x in char.filter_charms()
        ]


class ExaltedIntimacyForm(forms.Form):
    intimacy_1 = forms.CharField(max_length=100)
    intimacy_2 = forms.CharField(max_length=100)
    intimacy_3 = forms.CharField(max_length=100)
    intimacy_4 = forms.CharField(max_length=100)

    intimacy_strength_1 = forms.CharField(
        widget=forms.Select(
            choices=[("minor", "Minor"), ("major", "Major"), ("defining", "Defining"),]
        )
    )
    intimacy_strength_2 = forms.CharField(
        widget=forms.Select(
            choices=[("minor", "Minor"), ("major", "Major"), ("defining", "Defining"),]
        )
    )
    intimacy_strength_3 = forms.CharField(
        widget=forms.Select(
            choices=[("minor", "Minor"), ("major", "Major"), ("defining", "Defining"),]
        )
    )
    intimacy_strength_4 = forms.CharField(
        widget=forms.Select(
            choices=[("minor", "Minor"), ("major", "Major"), ("defining", "Defining"),]
        )
    )

    intimacy_type_1 = forms.CharField(
        widget=forms.Select(choices=[("tie", "Tie"), ("principle", "Principle"),])
    )
    intimacy_type_2 = forms.CharField(
        widget=forms.Select(choices=[("tie", "Tie"), ("principle", "Principle"),])
    )
    intimacy_type_3 = forms.CharField(
        widget=forms.Select(choices=[("tie", "Tie"), ("principle", "Principle"),])
    )
    intimacy_type_4 = forms.CharField(
        widget=forms.Select(choices=[("tie", "Tie"), ("principle", "Principle"),])
    )

    is_negative_1 = forms.BooleanField(required=False)
    is_negative_2 = forms.BooleanField(required=False)
    is_negative_3 = forms.BooleanField(required=False)
    is_negative_4 = forms.BooleanField(required=False)

    limit_trigger = forms.CharField(max_length=100)

    def has_intimacies(self):
        self.full_clean()
        has_four = all(self.cleaned_data[f"intimacy_{i}"] != "" for i in range(1, 5))
        strengths = [self.cleaned_data[f"intimacy_strength_{i}"] for i in range(1, 5)]
        one_defining = "defining" in strengths
        one_major = "major" in strengths
        one_negative = (
            self.cleaned_data["is_negative_1"]
            or self.cleaned_data["is_negative_2"]
            or self.cleaned_data["is_negative_3"]
            or self.cleaned_data["is_negative_4"]
        )
        return has_four and one_defining and one_major and one_negative


class ExaltedTotalForm(forms.Form):
    pass
