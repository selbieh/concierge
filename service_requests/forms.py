from django import forms

class RequestForm(forms.Form):
    clientName = forms.CharField(max_length=100)
    phoneNumber = forms.CharField(max_length=20)
    AgentName = forms.CharField(max_length=100)
    requestDetails=forms.CharField(max_length=300)
    requestDateTime = forms.DateTimeField()
    pickupAddress = forms.CharField(max_length=100)
    dropOffAddress = forms.CharField(max_length=100)
    notes = forms.CharField(max_length=300)