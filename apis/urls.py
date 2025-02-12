from .views import  *
from django.urls import path

urlpatterns = [

    path('get_users', GETUSERS.as_view(), name='get_users')
]