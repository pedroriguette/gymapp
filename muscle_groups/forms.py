from django import forms
from . import models


class MuscleGroupForm(forms.ModelForm):

    class Meta:
        model = models.MuscleGroups
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
