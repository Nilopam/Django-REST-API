from dataclasses import field
from .models import Emp, EmpProject,EmpSalary
from rest_framework import serializers

class EmpProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpProject
        fields = '__all__'

class EmpSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpSalary
        fields = '__all__'

class EmpSerializer(serializers.ModelSerializer):
    projects = EmpProjectSerializer(read_only = True, many = True)
    salary = EmpSalarySerializer(read_only = True, many = True)
    class Meta:
        model = Emp
        fields = '__all__'