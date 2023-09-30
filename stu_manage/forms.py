from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

class Student_reg(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        labels={"fname":"First Name","lname":"Last Name","email":"Email id"}
        widgets={"fname":forms.TextInput(attrs={"class":"form-control",}),
                 "lname":forms.TextInput(attrs={"class":"form-control",}),
                 "email":forms.TextInput(attrs={"class":"form-control",}),
                 "subject":forms.TextInput(attrs={"class":"form-control",}),}
        
class User_reg(UserCreationForm):
   
    class Meta:
        model=User
        fields=['username','first_name','last_name','email'] 
        labels={'first_name':'First Name','lastname':'Last Name'}
        widgets={'first_name':forms.TextInput(attrs={"class":'form-control'}),
                 'last_name':forms.TextInput(attrs={"class":'form-control'}),
                 'username':forms.TextInput(attrs={"class":'form-control'}),
                 'email':forms.TextInput(attrs={"class":'form-control'}),}       
        
        
class user_login(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))  
    password=UsernameField(widget=forms.PasswordInput(attrs={'class':'form-control'}))       