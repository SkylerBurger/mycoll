from django.urls import path

from .views import (
    ShowDetailView,
    ShowListView,
    SeasonDetailView,
    SeasonListView,
    SeasonCopyDetailView,
    SeasonCopyListView,
)


urlpatterns = [
    path('', ShowListView.as_view(), name='show_list'),
    path('<int:pk>', ShowDetailView.as_view(), name='show_detail'),
    path('season', SeasonListView.as_view(), name='season_list'),
    path('season/<int:pk>', SeasonDetailView.as_view(), name='season_detail'),
    path('season/copy', SeasonCopyListView.as_view(), name='season_copy_list'),
    path('season/copy/<int:pk>', SeasonCopyDetailView.as_view(), name='season_copy_detail'),
]
