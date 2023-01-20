# coding: utf-8

from rest_framework import serializers
import cms.models as c_m


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = c_m.Manufacturer
        fields = ('id', 'name',)#'__all__'


class CountrySerializer(serializers.ModelSerializer):
    manufacturers = ManufacturerSerializer(source='manufacturer_set', many=True)
    class Meta:
        model = c_m.Country
        fields = ('id', 'name', 'manufacturers')#'__all__'