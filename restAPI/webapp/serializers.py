from rest_framework import serializers
from .models import Educationtable

class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model= Educationtable
        fields ='__all__'