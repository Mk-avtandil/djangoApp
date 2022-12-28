from django import forms

from .models import Marvel


class PostForm(forms.ModelForm):
    class Meta:
        model = Marvel
        fields = ['name', 'slug', 'ability', 'gender', 'about', 'photo']

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'slug': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'ability': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'gender': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'about': forms.Textarea(
                attrs={'class': 'form-control'}
            ),
        }
