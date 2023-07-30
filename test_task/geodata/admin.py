from django.contrib import admin
from django.contrib.gis.db import models
from mapwidgets.widgets import GoogleStaticOverlayMapWidget
from leaflet.admin import LeafletGeoAdmin
from .models import Region, District, Canton, Contour


@admin.register(Region)
class RegionAdmin(LeafletGeoAdmin):
    list_display = ['title', 'geometry']
    formfield_overrides = {
        models.PolygonField: {'widget': GoogleStaticOverlayMapWidget},
    }


@admin.register(District)
class DistrictAdmin(LeafletGeoAdmin):
    list_display = ['title', 'geometry', 'region']
    formfield_overrides = {
        models.PolygonField: {'widget': GoogleStaticOverlayMapWidget},
    }


@admin.register(Canton)
class DistrictAdmin(LeafletGeoAdmin):
    list_display = ['title', 'geometry', 'district']
    formfield_overrides = {
        models.PolygonField: {'widget': GoogleStaticOverlayMapWidget},
    }


@admin.register(Contour)
class DistrictAdmin(LeafletGeoAdmin):
    list_display = ['geometry', 'canton']
    formfield_overrides = {
        models.PolygonField: {'widget': GoogleStaticOverlayMapWidget},
    }