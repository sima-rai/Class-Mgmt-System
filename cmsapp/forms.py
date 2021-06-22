from django import forms
from django.db import models
from django.db.models import fields
from django.forms.widgets import PasswordInput
from .models import *


class TeacherSignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Teacher
        fields = ['full_name', 'last_name', 'contact', 'address', 'school', 'username', 'email', 'password']
    
    def clean_username(self):
        uname = self.cleaned_data["username"]
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError("Customer with this username already exists")
        
        return uname

class TeacherLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=PasswordInput())

class StudentSignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Student
        fields = ['full_name', 'last_name', 'contact', 'address', 'school', 'grade', 'username', 'email', 'password']
    
    def clean_username(self):
        uname = self.cleaned_data["username"]
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError("Customer with this username already exists")
        
        return uname




    
