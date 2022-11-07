
from .models import Emp
from .serializers import EmpSerializer
from rest_framework import viewsets

# Create your views here.
class EmpViewSet(viewsets.ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer