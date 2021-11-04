from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)
from .views import MyObtainTokenPairView,RegisterView

#API routers
router = routers.DefaultRouter()
router.register('users',views.UsersView)

urlpatterns = [
  path('',views.home,name='home'),
  path('register/',views.register,name='register'),
  path('predictor/',views.prediction,name='predictor'),
  path('result/',views.result,name='result'),
  path('api/',include(router.urls)),#api url
  path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
  path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('user_registration/',RegisterView.as_view(),name='user_registration'),
]
