from django import forms

class AddForm(forms.Form):

    reg_number = forms.IntegerField(label="Enter Registration Number Of Kit",widget=forms.TextInput(attrs={'class':'form-control'}))
    name = forms.CharField(label="Name your culture!",max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    volume = forms.IntegerField(label='Enter Volume of culture(L)',widget = forms.TextInput(attrs={'class':'form-control'}))




