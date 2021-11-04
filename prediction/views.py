from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .serializers import UserSerializer,MyTokenObtainPairSerializer,RegisterSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .models import User
import joblib

# Create your views here.
def home(request): 
  return render(request,'index.html')

def register(request): 
  message=None
  if request.method == 'POST': 
    form = RegistrationForm(request.POST)
    if form.is_valid(): 
      user = form.save()
      message='User created'
      return redirect('/account/login/')
    else: 
      message='form is not valid'
  else: 
    form = RegistrationForm()
  return render(request,'two_factor/register.html',{"form":form})


# predictor views
def prediction(request):
  return render(request,"pred/predictor.html")

def result(request):
  cls = joblib.load('finalized_model.sav')

  lis = []
  
  lis.append(request.GET['Pregnancies'])
  lis.append(request.GET['Glucose'])
  lis.append(request.GET['BloodPressure'])
  lis.append(request.GET['SkinThickness'])
  lis.append(request.GET['Insulin'])
  lis.append(request.GET['BMI'])
  lis.append(request.GET['DiabetesPedigreeFunction'])
  lis.append(request.GET['Age'])

  ans = cls.predict([lis])
  return render(request,"pred/prediction.html",{'ans':ans, 'lis':lis})

  


#Users Api view
class UsersView(viewsets.ModelViewSet): 
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]
  
#Customized JWT Payload claim
class MyObtainTokenPairView(TokenObtainPairView): 
  permission_classes = (AllowAny,)
  serializer_class = MyTokenObtainPairSerializer
  
#User registration Api view
class RegisterView(generics.CreateAPIView): 
  queryset = User.objects.all()
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer