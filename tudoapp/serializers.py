from dataclasses import fields
from rest_framework import serializers
from .models import *

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tudumodels
        fields = "__all__" 
        
