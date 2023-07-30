# from django.db import models
from django.contrib.gis.db import models
from django_google_maps import fields as map_fields

# Create your models here.


class Region(models.Model):
    title = models.CharField('название региона', max_length=255)
    geometry = models.PolygonField('контур региона')


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='region_districts')
    title = models.CharField('название района', max_length=255)
    geometry = models.PolygonField('контур района')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class Canton(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district_cantons')
    title = models.CharField('название округа', max_length=255)
    geometry = models.PolygonField('контур округа')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Округ'
        verbose_name_plural = 'Округа'


class Contour(models.Model):
    canton = models.ForeignKey(Canton, on_delete=models.CASCADE, related_name='canton_contours')
    geometry = models.PolygonField('контур')
