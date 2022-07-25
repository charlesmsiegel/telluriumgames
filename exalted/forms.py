from django import forms


class RandomCharacterForm(forms.Form):
    character_type = forms.ChoiceField(choices=[("mortal", "Mortal"),])
    name = forms.CharField(max_length=100, label="Name", required=False)
    xp = forms.IntegerField(initial=0, label="XP")

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["character_type"].choices = []
