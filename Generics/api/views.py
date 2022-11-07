from django.shortcuts import render
from .models import Emp
from .serializers import EmpSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics,mixins
# Create your views here.

class EmpList(generics.ListCreateAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer


class EmpDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer