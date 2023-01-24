from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.
from django.core.mail import send_mail,BadHeaderError
from django.contrib.auth.models import AbstractBaseUser


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #department = models.CharField(max_length=100)
    #name = models.CharField(max_length=50,default="None")
    age=models.IntegerField(max_length=3,default=0)
    speciality=models.CharField(max_length=50,default="None")
    isfree=models.CharField(max_length=50,default="True")


    def __str__(self):
        return self.user.username
