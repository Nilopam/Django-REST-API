from django.shortcuts import render
from .models import Emp, EmpProject
from .serializers import EmpSerializer,EmpProjectSerializer
from rest_framework import generics
# Create your views here.

class EmpListView(generics.ListCreateAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

class EmpDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

class EmpProjectListView(generics.ListCreateAPIView):
    queryset = EmpProject.objects.all()
    serializer_class = EmpProjectSerializer

class EmpProjectDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmpProject.objects.all()
    serializer_class = EmpProjectSerializer
