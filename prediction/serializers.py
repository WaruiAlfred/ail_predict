from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

#Profile serializer class
class UserSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = User
    fields = ('id','username','email','is_superuser','is_active','is_admin','is_patient','is_health_practitioner','password',)
    
#JWT Custom payload claims apart from the default user_id
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_tokens(cls,user): 
    token = super(MyTokenObtainPairSerializer,cls).get_token(user)
    
    #Add custom claims
    token['username'] = user.username
    return token
  
#User registration serializer
class RegisterSerializer(serializers.ModelSerializer): 
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password1 = serializers.CharField(write_only=True,required=True,validators=[validate_password])
  password2 = serializers.CharField(write_only=True,required=True)
  
  class Meta: 
    model = User 
    fields = ('username','email','password1','password2','is_admin','is_patient','is_health_practitioner')
    
  def validate(self, attrs):
    if attrs['password1'] != attrs['password2']: 
      raise serializers.ValidationError({"password":"Password fields didn't match."})
    return attrs
  
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
      is_admin=validated_data['is_admin'],
      is_patient=validated_data['is_patient'],
      is_health_practitioner=validated_data['is_health_practitioner'],
    )
    
    user.set_password(validated_data['password1'])
    user.save()
    
    return user