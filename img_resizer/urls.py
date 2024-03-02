from django.urls import path

from .views import HistoryView, ResizeView, DownloadView

urlpatterns = [
    path("", ResizeView.as_view(), name="resize"),
    path("history/", HistoryView.as_view(), name="history"),
    path("download/<int:pk>/", DownloadView.as_view(), name="download"),
]
