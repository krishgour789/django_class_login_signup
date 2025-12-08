from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField( blank=True, null=True)
    contact = models.CharField(max_length=10, blank=True, null=True)
    detail = models.TextField( blank=True, null=True)
    gender = [
         ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    qualification = [
          ('10th', '10th'),
        ('12th', '12th'),
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate'),
    ]
    higher = [
             ('B.Sc', 'B.Sc'),
        ('B.A', 'B.A'),
        ('B.Tech', 'B.Tech'),
        ('M.Sc', 'M.Sc'),
        ('M.A', 'M.A'),
        ('M.Tech', 'M.Tech'),
        ('MBA', 'MBA'),
        ('PhD', 'PhD'),
        
    ]
    gender = models.CharField(max_length=10, choices=gender, blank=True, null=True)
    qualification = models.CharField(max_length=200, choices=qualification, blank=True, null=True)
    higher = models.CharField(max_length=100, choices=higher,blank=True, null=True)
    photo = models.ImageField(upload_to='images/',blank=True, null=True )
    document = models.ImageField(upload_to='doc/', blank=True, null=True)
    audio = models.FileField(upload_to='audio/', blank=True, null=True)
    video = models.FileField(upload_to='video/', blank=True, null=True)
    password = models.CharField(max_length=50,null=True)
class Query(models.Model):
    Name = models.CharField(max_length=50)
    Name = models.EmailField()
    Query = models.TextField()

    def __str__(self):
        return self.Query
