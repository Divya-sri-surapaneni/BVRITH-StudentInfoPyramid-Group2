from django.forms import ModelForm
from facultyapp.models import Comment

class ViewForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
