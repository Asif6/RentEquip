from cProfile import label
from dataclasses import fields
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm  
from .models.nuser import Nuser

class SignupForm(UserCreationForm):

    password1=forms.CharField(label="Password ",widget=forms.PasswordInput(attrs={"class":'form_control'}))
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={"class":'form_control'}))
    
    class Meta:       
        model=Nuser

        fields=['email','first_name','last_name','userName',]
        widgets={  "first_name":forms.TextInput({"class":'form_control'}),
                    "last_name":forms.TextInput({"class":'form_control'}),
                    "userName":forms.TextInput({"class":'form_control'}),
                    "email":forms.EmailInput({'class':"form_control"}),
                   
        }
        
        labels = {"email":'Email *',"first_name":"First Name *","last_name":'Last Name *','userName':'User Name'}

class LoginForm(forms.ModelForm):
    class Meta:
        model=Nuser

        fields=["email","password"]

        widgets={ "email":forms.EmailInput({"class":'form_control'}), "password":forms.PasswordInput({"class":'form_control'})}
        # error_massages={"email":{"unique":" THIS EMAIL IS ALLRADY "}}
        