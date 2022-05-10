from django import forms
from django.urls import reverse_lazy

# from characters.fields import ListTextWidget
from wod.models.characters.mage import Mage, MageFaction
from wod.models.locations.mage import Location


# Create your Forms here
class MageForm(forms.ModelForm):
    """Class that manages the form for creating and editing mages"""

    class Meta:
        """Meta class for the form"""

        model = Mage
        # fields = ("affiliation", "faction", "subfaction")
        fields = "__all__"
        # widgets = {
        #     "affiliation": forms.Select(
        #         attrs={"class": "col-sm btn btn-primary dropdown-toggle"}
        #     ),
        #     "faction": forms.Select(
        #         attrs={"class": "col-sm btn btn-primary dropdown-toggle"}
        #     ),
        #     "subfaction": forms.Select(
        #         attrs={"class": "col-sm btn btn-primary dropdown-toggle"}
        #     ),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["affiliation"].queryset = MageFaction.objects.filter(
            parent=None
        ).all()
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


class LocationForm(forms.ModelForm):
    """Class for Location Form"""

    class Meta:
        """Meta class for Location Form"""

        model = Location
        fields = ["name", "parent", "description"]
