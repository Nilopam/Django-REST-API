from django.shortcuts import render
from .models import Emp
from .serializers import EmpSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics,mixins
# Create your views here.

class EmpList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class EmpDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin ,generics.GenericAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
    
    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)