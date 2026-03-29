from django.db.models import Max
from rest_framework import generics

from .models import Url, UrlPing
from .serializers import UrlPingSerializer, UrlSerializer


class UrlListCreateView(generics.ListCreateAPIView):
    queryset = Url.objects.all().order_by("-created_at")
    serializer_class = UrlSerializer


class UrlLatestPingListView(generics.ListAPIView):
    serializer_class = UrlPingSerializer

    def get_queryset(self):

        latest_pings = UrlPing.objects.values("url").annotate(  # group by url
            latest=Max("time")
        )  # get latest time per url

        # fetch actual ping objects matching latest times
        result = []
        for entry in latest_pings:
            ping = UrlPing.objects.filter(
                url=entry["url"], time=entry["latest"]
            ).first()
            if ping:
                result.append(ping)

        return result
