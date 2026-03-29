from django.urls import path

from .views import UrlLatestPingListView, UrlListCreateView

app_name = "api"

urlpatterns = [
    path("urls/", UrlListCreateView.as_view(), name="url-list-create"),
    path("url-checks/", UrlLatestPingListView.as_view(), name="url-ping-list"),
]
