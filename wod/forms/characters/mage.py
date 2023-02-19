from django import forms

from core.fields import ListTextWidget
from wod.models.characters.human import MeritFlaw
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
