from django.urls import path

from .views import HistoryView, ResizeView, DownloadView

urlpatterns = [
    path("history/", HistoryView.as_view(), name="history"),
    path("", ResizeView.as_view(), name="resize"),
    path("download/<int:pk>/", DownloadView.as_view(), name="download"),
]
