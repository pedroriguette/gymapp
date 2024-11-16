from django import forms
from . import models


class CoachForm(forms.ModelForm):

    class Meta:
        model = models.Coach
        fields = [
            'user',
            'full_name',
            'birthday',
            'phone_number',
            'specialty',
            'entry',
            'start_job',
            'ends_job',
            'working_days',
            'status',
        ]
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Usuarios'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control'}),
            'entry': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }),
            'start_job': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'time',
                }),
            'ends_job': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'time',
                }),
            'working_days': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_user(self):
        user = self.cleaned_data.get('user')
        if models.Coach.objects.filter(user=user).exclude(pk=self.instance.pk).exists():
            self.add_error('user', 'Este Usuário já existe')
        return user
