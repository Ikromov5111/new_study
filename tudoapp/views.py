from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .serializers import TodoSerializers
from .models import Tudumodels
# Create your views here.

class TodoListApiView(ListAPIView):
    queryset = Tudumodels.objects.all()
    serializer_class = TodoSerializers
    
class TodoDetailApiView(RetrieveAPIView):
    queryset = Tudumodels.objects.all()
    serializer_class = TodoSerializers
     