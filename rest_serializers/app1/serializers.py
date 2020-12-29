from .models import Employe
from rest_framework import serializers




class Employee_S(serializers.ModelSerializer):
    class Meta:
        model = Employe
        # fields = ['name','age','address']
        fields = '__all__'


#
# class Employee_S(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     age = serializers.IntegerField()
#     address = serializers.CharField(max_length=100)
#
#     def create(self, validated_data):
#         return Employe.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.age = validated_data.get('age',instance.age)
#         instance.address = validated_data.get('address',instance.address)
#
#         instance.save()
#         return instance
