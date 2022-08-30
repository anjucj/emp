from django.db import models
from datetime import datetime



# Create your models here.



class Employee(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=200)
    email=models.EmailField()
    econtact=models.CharField(max_length=15)
    ecompany=models.CharField(max_length=100)

    def __str__(self):
        return self.ename


class Student(models.Model):
    
    sname=models.CharField(max_length=200)
    sreg=models.CharField(max_length=200)
    smark=models.CharField(max_length=15)
    
    def __str__(self):
        return self.sname