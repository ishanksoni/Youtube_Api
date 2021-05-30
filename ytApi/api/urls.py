from django.urls import path, include
from .views import *


urlpatterns = [
   path('', VideoList.as_view()) 
]
