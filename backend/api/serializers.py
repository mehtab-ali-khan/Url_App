from rest_framework import serializers
from .models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ["id", "url", "created_at"]
        read_only_fields = ["id", "created_at"]
