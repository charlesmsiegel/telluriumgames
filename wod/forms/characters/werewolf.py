from django import forms

from game.models.chronicle import Chronicle
from wod.models.characters.human import Archetype
from wod.models.characters.werewolf.garou import Tribe


class WerewolfCreationForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    concept = forms.CharField(label="Concept", max_length=100)
    chronicle = forms.ModelChoiceField(
        required=False,
        queryset=Chronicle.objects.filter(
            allowed_objects__name="Werewolf", allowed_objects__system="wod"
        ),
    )
    nature = forms.ModelChoiceField(queryset=Archetype.objects.all())
    demeanor = forms.ModelChoiceField(queryset=Archetype.objects.all())
    tribe = forms.ModelChoiceField(queryset=Tribe.objects.all())
    auspice = forms.ChoiceField(
        choices=[
            ("---", "---"),
            ("ragabash", "Ragabash"),
            ("theurge", "Theurge"),
            ("philodox", "Philodox"),
            ("galliard", "Galliard"),
            ("ahroun", "Ahroun"),
        ]
    )
    breed = forms.ChoiceField(
        choices=[
            ("---", "---"),
            ("homid", "Homid"),
            ("metis", "Metis"),
            ("lupus", "Lupus"),
        ],
    )
