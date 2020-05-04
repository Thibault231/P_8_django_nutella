from django import forms

class SubstituteForm(forms.Form):
    item_name = forms.CharField(
        label="Nom de l'aliment",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input-sm form-control'}),
        required=True
        )