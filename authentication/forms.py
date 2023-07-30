from django import forms



class LoginForm(forms.Form):
    email = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': "form-control", "placeholder": "Enter email address", "id":"exampleInputEmail1"}))
    password = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': "form-control", 'type': 'password', "placeholder": "•••••••••", "id":"exampleInputPassword1"}))