from django.urls import path
from .views import *
urlpatterns = [
    path('empdata/',empdata),
    path('emp_detail/<int:pk>/',emp_detail),

]