from django import forms

class AddForm(forms.Form):

    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    volume = forms.IntegerField(label='Enter Volume of culture(L)',widget = forms.TextInput(attrs={'class':'form-control'}))



