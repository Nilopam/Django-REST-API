from django.shortcuts import render
from .models import Emp, EmpProject,EmpSalary
from .serializers import EmpSerializer,EmpProjectSerializer,EmpSalarySerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.

class EmpPagination(PageNumberPagination):
    page_size = 2


class EmpListView(generics.ListCreateAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['mobile','address']


class EmpDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer


class EmpProjectListView(generics.ListCreateAPIView):
    queryset = EmpProject.objects.all()
    serializer_class = EmpProjectSerializer
    pagination_class = EmpPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['$project','$role']


class EmpProjectDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmpProject.objects.all()
    serializer_class = EmpProjectSerializer

    

class EmpSalaryListView(generics.ListCreateAPIView):
    queryset = EmpSalary.objects.all()
    serializer_class = EmpSalarySerializer
    pagination_class = EmpPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['e_name','salary']

class EmpSalaryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmpSalary.objects.all()
    serializer_class = EmpSalarySerializer

    