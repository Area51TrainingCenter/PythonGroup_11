from django import forms

class SearchForm(forms.Form):

    organization = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'nombre de organización'
            }
        )
    )