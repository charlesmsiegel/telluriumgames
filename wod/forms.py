from django import forms

from wod.models.characters.human import MeritFlaw
from wod.models.characters.mage import Mage, MageFaction
from core.fields import ListTextWidget


class RandomCharacterForm(forms.Form):
    gameline = forms.ChoiceField(
        choices=[
            ("choose", "Choose a Gameline"),
            ("werewolf", "Werewolf"),
            ("mage", "Mage"),
        ],
        initial=("gameline", "Choose a gameline"),
    )
    character_type = forms.ChoiceField(
        choices=[("werewolf", "Werewolf"), ("mage", "Mage")]
    )
    character_name = forms.CharField(max_length=100, label="Name", required=False)
    freebies = forms.IntegerField(initial=15)
    xp = forms.IntegerField(initial=0, label="XP")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["character_type"].choices = []


class RandomLocationForm(forms.Form):
    gameline = forms.ChoiceField(
        choices=[
            ("choose", "Choose a Gameline"),
            # ("werewolf", "Werewolf"),
            ("mage", "Mage"),
        ],
        initial=("gameline", "Choose a gameline"),
    )
    location_type = forms.ChoiceField(
        choices=[
            # ("werewolf", "Werewolf"),
            ("mage", "Mage")
        ]
    )
    name = forms.CharField(max_length=100, label="Name", required=False)
    rank = forms.IntegerField(initial=1, max_value=5)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["location_type"].choices = []


class RandomItemForm(forms.Form):
    gameline = forms.ChoiceField(
        choices=[
            ("choose", "Choose a Gameline"),
            # ("werewolf", "Werewolf"),
            ("mage", "Mage"),
        ],
        initial=("gameline", "Choose a gameline"),
    )
    item_type = forms.ChoiceField(choices=[("werewolf", "Werewolf"), ("mage", "Mage")])
    name = forms.CharField(max_length=100, label="Name", required=False)
    rank = forms.IntegerField(initial=1, max_value=5)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["item_type"].choices = []


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
        _resonance_list = kwargs.pop('data_list', None)
        super(ResonanceForm, self).__init__(*args, **kwargs)
        # the "name" parameter will allow you to use the same widget more than once in the same
        # form, not setting this parameter differently will cause all inputs display the
        # same list.
        self.fields['char_field_with_list'].widget = ListTextWidget(data_list=_resonance_list, name='resonance-list')
