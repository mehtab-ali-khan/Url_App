from django.urls import path

from .views import PingSnapshotView, UrlLatestPingListView, UrlListCreateView

app_name = "api"

urlpatterns = [
    path("urls/", UrlListCreateView.as_view(), name="url-list-create"),
    path("url-checks/", UrlLatestPingListView.as_view(), name="url-ping-list"),
    path(
        "pings/<int:pk>/snapshot/", PingSnapshotView.as_view(), name="get-ping-snapshot"
    ),
]
