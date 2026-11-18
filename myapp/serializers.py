from rest_framework import serializers
from .models import Student 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' # Include all fields of the student model in the serializer