from django.db import models

# Create your models here.
class Patients(models.Model):
    fname=models.CharField(max_length=50,default="None")
    lname=models.CharField(max_length=50,default="None")
    uname=models.CharField(max_length=50,default="None")
    email=models.EmailField(max_length=50,default="None")
    date=models.DateField()
    phone=models.IntegerField(max_length=11,default=0)
    city=models.CharField(max_length=100,default="None")
    state=models.CharField(max_length=100,default="None")
    symptoms=models.CharField(max_length=50,default="None")
    problem_in_breif=models.CharField(max_length=1000,default="None")
    bloodreport=models.ImageField(null=True,blank=True,upload_to="images/",default="")
    healthreport=models.ImageField(null=True,blank=True,upload_to="images/",default="")
    otherreport=models.ImageField(null=True,blank=True,upload_to="images/",default="")
    def __str__(self):
        return self.fname

