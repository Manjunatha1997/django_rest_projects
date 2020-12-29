from django.urls import path
from api_basic.views import *
urlpatterns = [
    path('al/',article_list),
    path('ad/<int:pk>/',article_detail),

]