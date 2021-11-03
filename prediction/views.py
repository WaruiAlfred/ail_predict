from django.shortcuts import render,redirect
from .forms import LoginForm,RegistrationForm

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

