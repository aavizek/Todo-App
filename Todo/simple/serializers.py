# This serializer class converts your model to JSON format
from rest_framework import serializers
from simple.models import Newdata

class NewdataSerializer(serializers.ModelSerializer):

    class Meta():
        model=Newdata
        fields='__all__'
