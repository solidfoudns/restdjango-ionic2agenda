__author__ = 'seader'
from .models import Orden
from rest_framework import serializers


class OrdenSerializer(serializers.ModelSerializer):


    class Meta:
        model = Orden
        fields = ('id', 'usuario', 'direccion', 'folio', 'fecha_evento')


