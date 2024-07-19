from django.db import models

# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=100)
    Couse=models.CharField(max_length=100)
    Gender=models.CharField(max_length=50)
    Dob=models.DateField()
    Address=models.CharField(max_length=200)
    Image=models.ImageField(upload_to='Student_Image/')