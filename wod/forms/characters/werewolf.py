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

class WerewolfAbilitiesForm(forms.Form):
    alertness = forms.IntegerField(max_value=3, min_value=0)
    athletics = forms.IntegerField(max_value=3, min_value=0)
    brawl = forms.IntegerField(max_value=3, min_value=0)
    empathy = forms.IntegerField(max_value=3, min_value=0)
    expression = forms.IntegerField(max_value=3, min_value=0)
    intimidation = forms.IntegerField(max_value=3, min_value=0)
    streetwise = forms.IntegerField(max_value=3, min_value=0)
    subterfuge = forms.IntegerField(max_value=3, min_value=0)
    leadership = forms.IntegerField(max_value=3, min_value=0)
    primal_urge = forms.IntegerField(max_value=3, min_value=0)

    crafts = forms.IntegerField(max_value=3, min_value=0)
    drive = forms.IntegerField(max_value=3, min_value=0)
    etiquette = forms.IntegerField(max_value=3, min_value=0)
    firearms = forms.IntegerField(max_value=3, min_value=0)
    melee = forms.IntegerField(max_value=3, min_value=0)
    stealth = forms.IntegerField(max_value=3, min_value=0)
    animal_ken = forms.IntegerField(max_value=3, min_value=0)
    larceny = forms.IntegerField(max_value=3, min_value=0)
    performance = forms.IntegerField(max_value=3, min_value=0)
    survival = forms.IntegerField(max_value=3, min_value=0)

    academics = forms.IntegerField(max_value=3, min_value=0)
    computer = forms.IntegerField(max_value=3, min_value=0)
    investigation = forms.IntegerField(max_value=3, min_value=0)
    medicine = forms.IntegerField(max_value=3, min_value=0)
    science = forms.IntegerField(max_value=3, min_value=0)
    enigmas = forms.IntegerField(max_value=3, min_value=0)
    law = forms.IntegerField(max_value=3, min_value=0)
    occult = forms.IntegerField(max_value=3, min_value=0)
    rituals = forms.IntegerField(max_value=3, min_value=0)
    technology = forms.IntegerField(max_value=3, min_value=0)

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")
        kwargs["initial"] = self.char.get_abilities()
        super().__init__(*args, **kwargs)

    def assign(self):
        self.full_clean()
        for key in (
            list(self.char.get_talents().keys())
            + list(self.char.get_skills().keys())
            + list(self.char.get_knowledges().keys())
        ):
            if key == "do" and self.char.faction.name != "Akashayana":
                pass
            else:
                setattr(self.char, key, self.cleaned_data[key])

    

    

    