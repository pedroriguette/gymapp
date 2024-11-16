from django import forms
from . import models


class StudentForm(forms.ModelForm):

    class Meta:
        model = models.Student
        fields = [
            'user',
            'full_name',
            'birthday',
            'phone_number',
            'objective',
            'frequency',
            'active',
            'photo',
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
            'objective': forms.TextInput(attrs={'class': 'form-control'}),
            'frequency': forms.NumberInput(attrs={'class': 'form-control'}),
            'active': forms.NullBooleanSelect(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_user(self):
        user = self.cleaned_data.get('user')
        if models.Student.objects.filter(user=user).exclude(pk=self.instance.pk).exists():
            self.add_error('user', 'Este Usuário já existe')
        return user
