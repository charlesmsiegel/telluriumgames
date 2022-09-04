from django import forms


class RandomCharacterForm(forms.Form):
    gameline = forms.ChoiceField(
        choices=[("choose", "Choose a Gameline"), ("core", "Core"), ("mage", "Mage"),],
        initial=("gameline", "Choose a gameline"),
    )
    character_type = forms.ChoiceField(choices=[("core", "Core"), ("mage", "Mage")])
    name = forms.CharField(max_length=100, label="Name", required=False)
    xp = forms.IntegerField(initial=0, label="XP")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["character_type"].choices = []
