# from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser): 
  is_admin = models.BooleanField('Admin',default=False)
  is_patient = models.BooleanField('Patient',default=False)
  is_health_practitioner = models.BooleanField('Health practitioner',default=False)