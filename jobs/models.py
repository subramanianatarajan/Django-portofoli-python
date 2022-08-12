from django.db import models

# Create your models here.
class job (models.Model):
    #Images
    image = models.ImageField(upload_to = 'images/')
    #summary job details
    summary=models.CharField(max_length=600)


    def __str__(self):
         return self.summary