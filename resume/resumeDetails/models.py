from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class ResumeInfo(models.Model):
   Full_name = models.CharField(max_length=255)
   phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
   Phone_number = models.CharField(max_length=15,validators=[phone_regex], blank=True) # validators should be a list
   Email = models.EmailField(max_length=25) 
   Current_city = models.CharField(max_length=10)
   Graduation_percent = models.FloatField()
   Twelth_percent = models.FloatField()
   Tenth_percent = models.FloatField()
   Job_expr = models.TextField()
   Technicalskills = models.CharField(max_length=500)
   Projects = models.CharField(max_length=500)
   Achievements = models.CharField(max_length=100)
   Workshops = models.CharField(max_length=500)
   Internships = models.CharField(max_length=300)
   Github = models.TextField()
   Add = models.TextField()

   def __str__(self):
      return self.Technicalskills
