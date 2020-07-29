from django.urls import path

from .views import (
    ShowDetailView,
    ShowListView,
    SeasonDetailView,
    SeasonCopyDetailView,
)


urlpatterns = [
    path('', ShowListView.as_view(), name='show_list'),
    path('<int:pk>', ShowDetailView.as_view(), name='show_detail'),
    path('season/<int:pk>', SeasonDetailView.as_view(), name='season_detail'),
    path('season/copy/<int:id>', SeasonCopyDetailView.as_view(), name='season_copy_detail'),
]
