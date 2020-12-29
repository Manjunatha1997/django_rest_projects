from .models import *
from rest_framework import serializers

class EmpS(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = '__all__'
