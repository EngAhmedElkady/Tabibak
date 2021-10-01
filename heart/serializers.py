from rest_framework import serializers
from heart.models import *
from django.contrib.auth.models import User
# Serializers define the API representation.

class Heart_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heart
        fields ='__all__'