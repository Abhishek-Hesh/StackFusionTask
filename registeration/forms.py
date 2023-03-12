from django.forms import ModelForm, Textarea
from django import forms
from .models import Person
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Mainform(ModelForm):
    # user_name = forms.CharField(label='Name', max_length=20, min_length=4)
    class Meta:
        model = Person
        fields = ['name', 'dob', 'email', 'phone_no']
        widgets = {
                'name' : forms.TextInput(attrs={'type' : "text", "class" : "form-control" 
                ,"aria-describedby" : "fname", "placeholder" : "First Name " ,"Name" :"fname"}),
                'dob' : forms.DateInput(attrs={'type' : "date", "class" : "form-control", 'required pattern' : "\d{4}-\d{2}-\d{2}" 
                ,"aria-describedby" : "dob", "placeholder" : "yyyy-mm-dd" ,"name" :"Date Of Birth" ,'min':'1959-01-01'}),
                'email' : forms.TextInput(attrs={'type' : "email", "class" : "form-control" 
                ,"aria-describedby" : "email", "placeholder" : "Enter email" ,"name" :"email"}),
                'phone_no' : forms.NumberInput(attrs={'type' : "numeric", "class" : "form-control" 
                ,"aria-describedby" : "phone_no", "placeholder" : "Phone no" ,"name" :"Phone_no"})
        }
    def save(self, commit=True):
        user = super(Mainform, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
