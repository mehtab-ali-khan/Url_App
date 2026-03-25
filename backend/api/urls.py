from django.urls import path

from .views import UrlListCreateView

app_name = "api"

urlpatterns = [
    path("urls/", UrlListCreateView.as_view(), name="url-list-create"),
]
