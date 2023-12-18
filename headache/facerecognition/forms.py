from pyexpat import model
from django.forms import ModelForm
# from .models import Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# class OrderForm(ModelForm):
#     class Meta:
#         model=Order
#         fields ='__all__'




class usernameForm(forms.Form):
	username=forms.CharField(max_length=30)




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username','email', 'password1', 'password2']







         
# class CreateUserForm(forms.Form):
#     username= forms.CharField(max_length=100,
#                            widget= forms.TextInput
#                            (attrs={'placeholder':'Full name'}))
#     email= forms.CharField(max_length=100,
#                            widget= forms.EmailInput
#                            (attrs={'placeholder':'Email'}))
#     password1= forms.CharField(max_length=100,
#                            widget= forms.PasswordInput
#                            (attrs={'placeholder':'Password'}))
#     password2= forms.CharField(max_length=100,
#                            widget= forms.PasswordInput
#                            (attrs={'placeholder':'Confirm Password'}))