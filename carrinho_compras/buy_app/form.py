from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import BuyModel




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class BuyForms(forms.ModelForm):
    class Meta:
        model = BuyModel
        fields = ["name_product", "price", "amount"]