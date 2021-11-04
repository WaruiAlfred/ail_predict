# from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser): 
  is_admin = models.BooleanField('Admin',default=False)
  is_patient = models.BooleanField('Patient',default=False)
  is_health_practitioner = models.BooleanField('Health practitioner',default=False)

class Diabetes(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  Pregnancies = models.IntegerField()
  Glucose = models.IntegerField()
  BloodPressure = models.IntegerField()
  SkinThickness = models.IntegerField()
  Insulin = models.IntegerField()  
  BMI= models.IntegerField()  
  DiabetesPedigreeFunction = models.IntegerField()
  Age = models.IntegerField()

  def __str__(self):
    self.user.username

  
  

