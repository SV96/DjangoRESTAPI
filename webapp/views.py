from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from webapp.models import employee
from . serializers import employeeSerializers
# Create your views here.

class employeeList(APIView):

    def get(self,request):
        employees1 = employee.objects.all()
        # conver all data to json and say that there are many data so take all
        serializer = employeeSerializers(employees1,many=True) 
        return Response(serializer.data)
    def post(self):
        pass