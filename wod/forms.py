from django import forms

class RandomCharacterForm(forms.Form):
    gameline = forms.ChoiceField(choices=[("choose", "Choose a Gameline"), ("werewolf", "Werewolf"), ("mage", "Mage")], initial=("gameline", "Choose a gameline"))
    character_type = forms.ChoiceField(choices=[("werewolf", "Werewolf"), ("mage", "Mage")])
    character_name = forms.CharField(max_length=100, label="Name", required=False)
    freebies = forms.IntegerField(initial=15)
    xp = forms.IntegerField(initial=0, label="XP")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['character_type'].choices = []
