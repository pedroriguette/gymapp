from django import forms
from . import models


class ExerciceForm(forms.ModelForm):

    class Meta:
        model = models.Exercice
        fields = [
            "name",
            "category",
            "muscle_groups",
            "difficulty_level",
            "equipment",
            "photo",
            "description"
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'muscle_groups': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'difficulty_level': forms.Select(attrs={'class': 'form-control'}),
            'equipment': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput({'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'name': 'Nome',
            'category': 'Categoria',
            'muscle_groups': 'Grupos Musculares',
            'difficulty_level': 'Nivél de dificuldade',
            'equipment': 'Equipamento',
            'photo': 'Foto',
            'description': 'Descrição',
        }
