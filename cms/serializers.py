# coding: utf-8

from rest_framework import serializers
import cms.models as c_m


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = c_m.Country
        fields = ('id', 'name')