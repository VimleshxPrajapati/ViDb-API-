from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import Registration_view,logout_view

urlpatterns = [
    path('login/',obtain_auth_token,name='login'),
    path('register/',Registration_view,name='register'),
    path('logout/',logout_view,name='logout')
]
