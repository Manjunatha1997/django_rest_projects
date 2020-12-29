from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employe
from . serializers import Employee_S
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import *
# Create your views here.

@api_view(['GET','POST'])
def empdata(request):
    if request.method == 'GET':
        emp_data = Employe.objects.all()
        serializer = Employee_S(emp_data,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Employee_S(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

@api_view(['GET','PUT','DELETE'])
def emp_detail(request,pk):
    try:
        data = Employe.objects.get(pk=pk)
    except:
        return Response(status=HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = Employee_S(data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Employee_S(data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=HTTP_204_NO_CONTENT)



# def empdata(request):
#     if request.method == 'GET':
#         emp_data = Employe.objects.all()
#         serializer = Employee_S(emp_data,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method == 'POST':
#         serializer = Employee_S(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors,status=400)


# @csrf_exempt
# def empdata(request):
#     if request.method == 'GET':
#         emp_data = Employe.objects.all()
#         serializer = Employee_S(emp_data,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = Employee_S(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors,status=400)
#
