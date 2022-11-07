from django.shortcuts import render
from .serializers import EmpSerializer
from .models import Emp 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET','POST'])
def emp_list(request):

    if request.method == "GET":
        e = Emp.objects.all()
        s = EmpSerializer(e,many=True)
        return Response(s.data)

    elif request.method == "POST":
        s = EmpSerializer(data = request.data)
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)
        else :
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def emp_details(request,pk):
    try:
        e = Emp.objects.get(pk=pk)
    except Emp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        s =EmpSerializer(e)
        return Response(s.data)
    
    elif request.method == "PUT":
        s = EmpSerializer(e,data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        e.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

