from django import forms

class SubstituteForm(forms.Form):
    item_name = forms.CharField(
        label="Nom de l'aliment",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input-sm form-control'}),
        required=True
        )

class ConnexionForm(forms.Form):
    username = forms.CharField(label="User name:", max_length=30)
    password = forms.CharField(label="Password:", widget=forms.PasswordInput)

class CountCreationForm(forms.Form):
    username = forms.CharField(label="User name:", max_length=30)
    first_name = forms.CharField(label="First_name:", max_length=50)
    last_name = forms.CharField(label="Last_name:", max_length=50)
    email = forms.EmailField(label="E-mail:")
    password1 = forms.CharField(label="Password:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password:", widget=forms.PasswordInput)