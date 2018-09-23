from django import forms


class FormularioRepo(forms.Form):
    fil = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }
        )
    )