from rest_framework import serializers

from .models import Url, UrlPing


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ["id", "url", "created_at"]
        read_only_fields = ["id", "created_at"]


class UrlPingSerializer(serializers.ModelSerializer):
    url_string = serializers.CharField(source="url.url", read_only=True)

    class Meta:
        model = UrlPing
        fields = ["id", "url", "url_string", "status_code", "time"]
        read_only_fields = ["id", "time"]
