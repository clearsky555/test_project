from django.urls import path

from . import views


urlpatterns = [
    path('regions/', views.RegionListAPIView.as_view()),
    path('districts/', views.DistrictListAPIView.as_view()),
    path('cantons/', views.CantonListAPIView.as_view()),
]