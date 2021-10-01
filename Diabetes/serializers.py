from rest_framework import serializers
from Diabetes.models import *
from django.contrib.auth.models import User
# Serializers define the API representation.

class Diabets_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diabets
        fields ='__all__'