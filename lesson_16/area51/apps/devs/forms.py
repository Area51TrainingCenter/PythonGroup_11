from django import forms


class FormDeveloper(forms.Form):

    name = forms.CharField()

    lastname = forms.CharField()

    email = forms.EmailField()

