from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('data',EmpViewset,basename='data')
router.register('EmpGenericViewset',EmpGenericViewset,basename='EmpGenericViewset')


urlpatterns = [

    path('viewsets/',include(router.urls)),
    path('viewsets/<int:pk>/',include(router.urls)),
    path('viewsets/',include(router.urls)),

    path('empdata/',empdata),
    path('emp_detail/<int:pk>/',emp_detail),
    path('EmpAPIView/',EmpAPIView.as_view()),
    path('EmpDetailAPIView/<int:pk>/',EmpDetailAPIView.as_view()),
    path('GenericAPIView/',GenericAPIView.as_view()),
    path('GenericAPIViewDetail/<int:pk>/',GenericAPIViewDetail.as_view()),

]
