from django import forms
from game.models import Story
from core.models import LocationModel

class SceneCreationForm(forms.Form):
    name = forms.CharField(max_length=100)
    location = forms.ModelChoiceField(queryset=LocationModel.objects.order_by("name"))
    
    def __init__(self, *args, **kwargs):
        chronicle = kwargs.pop("chronicle")
        super().__init__(*args, **kwargs)
        self.fields["location"] = forms.ModelChoiceField(
            LocationModel.objects.filter(chronicle=chronicle).order_by("name")
        )

class StoryCreationForm(forms.Form):
    name = forms.CharField(max_length=100)
    
class AddCharForm(forms.Form):
    pass

class PostForm(forms.Form):
    pass
