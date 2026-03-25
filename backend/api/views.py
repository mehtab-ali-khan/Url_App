from rest_framework import generics

from .models import Url
from .serializers import UrlSerializer


class UrlListCreateView(generics.ListCreateAPIView):
    queryset = Url.objects.all().order_by("-created_at")
    serializer_class = UrlSerializer
