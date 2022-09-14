from django import forms


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
