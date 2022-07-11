from django import forms
from wod.models.characters.mage import Mage, MageFaction
from wod.models.characters.human import MeritFlaw, Specialty


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


class MageForm(forms.ModelForm):
    strength_specs = Specialty.objects.filter(stat="strength")
    num_strength_specs = strength_specs.count()
    strength_specialty = forms.MultipleChoiceField(choices=zip(range(num_strength_specs), Specialty.objects.filter(stat="strength")))
    
    class Meta:
        model = Mage
        fields = "__all__"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["merits_and_flaws"].queryset = MeritFlaw.objects.filter(
            pk__in=[x.id for x in MeritFlaw.objects.all() if "mage" in x.allowed_types]
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
