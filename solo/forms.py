from django import forms

class postQuery(forms.Form):
    query = forms.CharField(max_length=256)