from django import forms


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
