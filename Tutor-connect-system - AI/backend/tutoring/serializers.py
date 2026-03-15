from rest_framework import serializers
from .models import TuitionRequest

class TuitionSerializer(serializers.ModelSerializer):

    class Meta:

        model = TuitionRequest
        fields = "__all__"