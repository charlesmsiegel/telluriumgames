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
    def __init__(self, *args, **kwargs):
        char = kwargs.pop("character")
        super().__init__(*args, **kwargs)

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
