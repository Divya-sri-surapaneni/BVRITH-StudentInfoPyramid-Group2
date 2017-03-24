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

    class Meta:
        model = ResumeInfo
        fields = ( 'technicalskills','projects','achievements', 'workshops','internships')
        

