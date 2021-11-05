from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .serializers import UserSerializer,MyTokenObtainPairSerializer,RegisterSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .models import User
from .email import send_welcome_email

# Create your views here.
def home(request): 
  return render(request,'index.html')

def register(request): 
  message=None
  if request.method == 'POST': 
    form = RegistrationForm(request.POST)
    if form.is_valid(): 
      name = form.cleaned_data['username']
      email = form.cleaned_data['email']
      user = form.save()
      send_welcome_email(name,email)
      message='User created'
      return redirect('/account/login/')
    else: 
      message='form is not valid'
  else: 
    form = RegistrationForm()
  return render(request,'two_factor/register.html',{"form":form})

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