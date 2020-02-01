from django import forms
from django.contrib.auth.models import User
from farmers.models import Farmer

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['quantity', 'crop_name', 'time_type',]
