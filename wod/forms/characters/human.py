from django import forms

from wod.models.characters.human import MeritFlaw


class AttributeForm(forms.Form):
    strength = forms.IntegerField(max_value=5, min_value=1)
    dexterity = forms.IntegerField(max_value=5, min_value=1)
    stamina = forms.IntegerField(max_value=5, min_value=1)
    charisma = forms.IntegerField(max_value=5, min_value=1)
    manipulation = forms.IntegerField(max_value=5, min_value=1)
    appearance = forms.IntegerField(max_value=5, min_value=1)
    perception = forms.IntegerField(max_value=5, min_value=1)
    intelligence = forms.IntegerField(max_value=5, min_value=1)
    wits = forms.IntegerField(max_value=5, min_value=1)

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")
        kwargs["initial"] = self.char.get_attributes()
        super().__init__(*args, **kwargs)

    def assign(self):
        self.full_clean()
        self.char.strength = self.cleaned_data["strength"]
        self.char.dexterity = self.cleaned_data["dexterity"]
        self.char.stamina = self.cleaned_data["stamina"]
        self.char.charisma = self.cleaned_data["charisma"]
        self.char.manipulation = self.cleaned_data["manipulation"]
        self.char.appearance = self.cleaned_data["appearance"]
        self.char.perception = self.cleaned_data["perception"]
        self.char.intelligence = self.cleaned_data["intelligence"]
        self.char.wits = self.cleaned_data["wits"]
        
class MeritFlawForm(forms.Form):
    mf = forms.ModelChoiceField(queryset=MeritFlaw.objects.none())
    rating = forms.ChoiceField(choices=[("---", "---")])
    
    def __init__(self, *args, **kwargs):
        chartype = kwargs.pop('chartype')
        tmp = {chartype: True}
        super().__init__(*args, **kwargs)
        self.fields['mf'].queryset = MeritFlaw.objects.filter(**tmp)
