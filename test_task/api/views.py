from django.shortcuts import render

from rest_framework.generics import ListAPIView
from api.serializers import RegionSerializer, DistrictSerializer, CantonSerializer
from geodata.models import Region, District, Canton


class RegionListAPIView(ListAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class DistrictListAPIView(ListAPIView):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()


class CantonListAPIView(ListAPIView):
    serializer_class = CantonSerializer
    queryset = Canton.objects.all()