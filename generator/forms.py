from django import forms


class HomePageForm(forms.Form):
    Length = forms.IntegerField(min_value=8, max_value=40)
    Upper = forms.BooleanField(required=False)
    Lower = forms.BooleanField(required=False)
    Numbers = forms.BooleanField(required=False)
    Special = forms.BooleanField(required=False)

