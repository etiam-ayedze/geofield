from django import forms
from .models import Region


class region_form(forms.ModelForm):
    class Meta:
        model = Region
        fields = "__all__"


