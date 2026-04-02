from rest_framework import serializers

from .models import Url, UrlPing


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ["id", "url", "created_at"]
        read_only_fields = ["id", "created_at"]


class UrlPingSerializer(serializers.ModelSerializer):
    url_string = serializers.CharField(source="url.url", read_only=True)
    has_snapshot = serializers.SerializerMethodField()

    class Meta:
        model = UrlPing
        fields = ["id", "url", "url_string", "status_code", "time", "has_snapshot"]
        read_only_fields = ["id", "time"]

    def get_has_snapshot(self, obj):
        return obj.error_snapshot is not None
