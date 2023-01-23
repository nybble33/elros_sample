# coding: utf-8

from rest_framework import serializers
import cms.models as c_m


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = c_m.Comment
        fields = ('author_email', 'vehicle', 'post_date', 'text')


class VehicleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(
        source='comment_set',
        many=True,
        read_only=True,
        )
    class Meta:
        model = c_m.Vehicle
        fields = ('id', 'name', 'manufacturer', 'start_year', 'end_year', 'comments')

    def validate(self, data):
        if data['start_year'] > data['end_year']:
            raise serializers.ValidationError("end must occur after start")
        return data


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = c_m.Manufacturer
        fields = ('id', 'name', 'country')


class CountrySerializer(serializers.ModelSerializer):
    manufacturers = ManufacturerSerializer(
        source='manufacturer_set',
        many=True,
        read_only=True,
        )
    class Meta:
        model = c_m.Country
        fields = ('id', 'name', 'manufacturers')