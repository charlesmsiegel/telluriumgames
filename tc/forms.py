from django import forms

from tc.models import Aberrant


# Create your Forms here
class AberrantForm(forms.ModelForm):
    class Meta:
        model = Aberrant
        fields = "__all__"
