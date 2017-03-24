'''from django.forms import ModelForm

from .models import PersonalInfo

class RegistrationForm(ModelForm):

    class Meta:
        model = PersonalInfo
        fields = '__all__'
'''
from django import forms

from .models import ResumeInfo

class DetailForm(forms.ModelForm):
    Full_name = forms.CharField()
    Current_city = forms.CharField()
    Technicalskills = forms.CharField()
    Projects = forms.CharField()
    Achievements = forms.CharField()
    Workshops = forms.CharField()
    Internships = forms.CharField()


    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                                error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    Email       = forms.EmailField(widget=forms.EmailInput({'placeholder': 'test@example.com'}))
    Job_expr = forms.CharField(widget=forms.Textarea)
    Github = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ResumeInfo
        
        fields = "__all__"

        

