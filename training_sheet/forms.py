from django import forms
from . import models


class TrainingSheetForm(forms.ModelForm):

    class Meta:
        model = models.TrainingSheet
        fields = [
            'student',
            'coach',
            'exercice',
            'series',
            'repetitions',
            'time',
            'group',
        ]
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'coach': forms.Select(attrs={'class': 'form-control'}),
            'exercice': forms.Select(attrs={'class': 'form-control'}),
            'series': forms.NumberInput(attrs={'class': 'form-control'}),
            'repetitions': forms.NumberInput(attrs={'class': 'form-control'}),
            'time': forms.NumberInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }
