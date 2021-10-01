from rest_framework import serializers
from kidney.models import *
from django.contrib.auth.models import User
# Serializers define the API representation.

class person_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kidney
        fields ='__all__'