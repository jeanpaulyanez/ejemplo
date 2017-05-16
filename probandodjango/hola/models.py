from __future__ import unicode_literals

from django.db import models

class TIPO_ORIGEN(models.Model):
    TIPO_ORIGEN = models.CharField(max_length=5, primary_key=True)
    DESCRIPCION = models.CharField(max_length=100, null = True)
    class Meta:
         db_table = "TIPO_ORIGEN"
         
class WEB_GEO(models.Model):
    SEPULTURA = models.CharField(max_length=5, primary_key=True)
    SECTOR = models.CharField(max_length=100, null = True)
    class Meta:
         db_table = "WEB_GEO"         