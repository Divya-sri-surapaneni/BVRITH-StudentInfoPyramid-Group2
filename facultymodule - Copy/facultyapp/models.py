from django.db import models


class Comment(models.Model):
      
      Student_ID = models.CharField(max_length=200)
      Suggestions = models.TextField()

      def __str__(self):
            return self.Student_ID



     
