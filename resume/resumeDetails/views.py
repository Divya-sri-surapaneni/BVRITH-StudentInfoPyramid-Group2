from django.shortcuts import render
from .models import ResumeInfo

from .forms import DetailForm
from django.http import HttpResponse
# Create your views here.

def register(request):
    return HttpResponse("Welcome to student info system")
def success(request):
    return HttpResponse("Entered Succefully")

def post_new(request):
    if request.method=='GET':
       form = DetailForm()
       return render(request, 'resumeDetails/register.html', {'form': form})
    elif request.method=='POST':
       form=DetailForm(request.POST)
       if form.is_valid():
          ResumeInfo = form.save(commit=False)
          ResumeInfo.save()
          return success(form)

'''def index(request):
   details=PersonalInfo.objects.all()
   return render(request,'StudentDetails/index.html', {'details':details})
'''
'''def registrationform(request):
   form = RegistrationForm()
   if form.is_valid():
      PersonalInfo = form.save(commit=False)
      PersonalInfo .firstname = request.user
      PersonalInfo .secondname = request.user
      PersonalInfo .save()
   return render(request, 'StudentDetails/index.html', {'form': form})
'''

