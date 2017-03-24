from django.db import models

# Create your models here.
class ResumeInfo(models.Model):
   technicalskills = models.CharField(max_length=500)
   projects = models.CharField(max_length=500)
   achievements = models.CharField(max_length=100)
   workshops = models.CharField(max_length=500)
   internships = models.CharField(max_length=300)
   
   def __str__(self):
      return self.technicalskills
