from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Educationtable
from .serializers import EducationSerializer

# Create your views here.
class educationList(APIView) :
    def get(self,request):
        education1 = Educationtable.objects.all()
        serializer= EducationSerializer(education1, many=True)
        return Response(serializer.data)

    def post(self):
        pass





