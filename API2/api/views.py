from django.shortcuts import render
from .serializers import EmpSerializer
from .models import Emp 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.

class EmpList(APIView):

    def get(self,request):
     if request.method == "GET":
        e = Emp.objects.all()
        s = EmpSerializer(e,many=True)
        return Response(s.data)

    def post(self,request):
        s = EmpSerializer(data = request.data)
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)
        else :
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

class EmpDetails(APIView):

    def get_object(self,pk):
        try:
            return Emp.objects.get(pk=pk)
        except Emp.DoesNotExist:
            raise Http404

    def get(self,request,pk):
       e =  self.get_object(pk)
       s = EmpSerializer(e)
       return Response(s.data)

    def put(self,request,pk):
       e =  self.get_object(pk)
       s = EmpSerializer(e,data=request.data)
       if s.is_valid():
            s.save()
            return Response(s.data)

       else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        e =  self.get_object(pk)
        e.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        
