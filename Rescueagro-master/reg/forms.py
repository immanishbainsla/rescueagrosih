from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from reg.models import Organisation,address1, Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class organisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ['phone_no','Name','organisations']


class PostForm(forms.ModelForm):
    finaltime = forms.CharField(widget = forms.TextInput(
    attrs = {
        'placeholder': '',
        'value': '2020-03-10 11:01:25'
    }))
    class Meta:
        model = Post
        fields = ['name', 'type', 'amount', 'description', 'finaltime', 'landmark', 'town', 'dist', 'state', 'pin', 'mobile']


class addressForm(forms.ModelForm):
    house = forms.CharField(widget = forms.TextInput(
    attrs = {
        'placeholder': 'House/Building/Apt'
    }))
    street = forms.CharField(widget = forms.TextInput(
    attrs = {
        'placeholder': 'Street/Road/Lane'
    }))
    area = forms.CharField(widget = forms.TextInput(
    attrs = {
        'placeholder': 'Area/Locality/Sector'
    }))
    class Meta:
        model = address1
        fields = ['house','street','area','pincode','district','state']
