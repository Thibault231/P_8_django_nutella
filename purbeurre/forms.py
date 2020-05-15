# coding: utf-8
"""Create formular for Purbeurre
templates and views.
"""
from django import forms


class SubstituteForm(forms.Form):
    """Formular Class Form.
    Use in PurBeurre templates and views.
    """
    item_name = forms.CharField(
        label="Nom de l'aliment",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input-sm form-control'}),
        required=True
        )
