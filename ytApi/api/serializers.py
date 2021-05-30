from rest_framework import serializers
from .models import *


# Serializers Class for Video data model.
class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = "__all__"
        