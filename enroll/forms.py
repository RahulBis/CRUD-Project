from django import forms
from .models import Signup

class stu_signup(forms.ModelForm):
    class Meta:
        model = Signup
        fields =['id','username','first_name','last_name','email','password']
        widgets ={
            'id': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Id'}),
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
        }