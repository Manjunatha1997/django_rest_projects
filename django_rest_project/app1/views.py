from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import *
from .serializer import *
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,mixins
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
# Create your views here.

# class EmpGenericViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     serializer_class = EmpS
#     queryset = Emp.objects.all()
class EmpGenericViewset(viewsets.ModelViewSet):
    serializer_class = EmpS
    queryset = Emp.objects.all()



class EmpViewset(viewsets.ViewSet):
    def list(self,request):
        emp_data = Emp.objects.all()
        serializer = EmpS(emp_data,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = EmpS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        query_set = Emp.objects.all()
        emp_data = get_object_or_404(query_set,pk=pk)
        serializer = EmpS(emp_data)
        return Response(serializer.data)

    def update(self,request,pk=None):
        try:
            emp_data = Emp.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = EmpS(emp_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_204_NO_CONTENT)

    def destroy(self,request,pk=None):
        emp_data = Emp.objects.get(pk=pk)
        emp_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class = EmpS
    queryset = Emp.objects.all()
    # authentication_classes = [SessionAuthentication,BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)



class GenericAPIViewDetail(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = EmpS
    queryset = Emp.objects.all()
    lookup_field = 'pk'
    def get(self,request,pk):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)
    def put(self,request,pk=None):
        return self.update(request,pk)
    def delete(self, request, pk):
        return self.destroy(request)





# @permission_classes([IsAuthenticated,IsAdminUser])
class EmpAPIView(APIView):
    def get(self,request):
        emp_data = Emp.objects.all()
        serializer = EmpS(emp_data,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = EmpS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EmpDetailAPIView(APIView):
    def get_object(self,pk):
        try:
            return Emp.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        try:
            empdata = self.get_object(pk)
            serializer = EmpS(empdata)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        empdata = self.get_object(pk)
        serializer = EmpS(empdata,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        empdata = self.get_object(pk)
        empdata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST'])
@permission_classes ([IsAuthenticated])
def empdata(request):
    if request.method == 'GET':
        emp_data = Emp.objects.all()
        serializer = EmpS(emp_data,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmpS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def emp_detail(request,pk):
    try:
        emp_data = Emp.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmpS(emp_data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmpS(emp_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        emp_data.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

