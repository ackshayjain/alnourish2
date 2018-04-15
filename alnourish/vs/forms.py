from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    comments = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
