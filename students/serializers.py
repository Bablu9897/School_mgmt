from rest_framework import serializers
from .models import *



class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = '__all__'
        
        
    def create(self, validated_data):
        return StudentInfo.objects.create(**validated_data)