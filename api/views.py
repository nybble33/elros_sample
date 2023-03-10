from django.shortcuts import render

# Create your views here.

from json2xml import json2xml
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

import cms.serializers as c_s
import cms.models as c_m


class CountryView(APIView):

    def get(self, request):
        context = {}
        try:
            _country_object = c_m.Country.objects.get(
                                pk=request.query_params['id']
                                )
        except c_m.Country.DoesNotExist:
            return JsonResponse(
                {'result': 'The country does not exist'},
                )
        _country = c_s.CountrySerializer(
            _country_object
        ).data
        context['country'] = _country
        if 'export' in request.query_params:
            if request.query_params['export'] == 'xml':
                _c = c_m.Country.objects.all()
                _export_response = json2xml.Json2xml(_country).to_xml()
                return HttpResponse(_export_response)
        return Response(context)

    def post(self, request):
        context = {}
        _country_serializer = c_s.CountrySerializer(data=request.query_params)
        if _country_serializer.is_valid(raise_exception=True):
            _country_serializer.save()
            context['result'] = f'Country {request.query_params["name"]} was created'
        else:
            context['result'] = 'error'
        return Response(context)

    def put(self, request):
        context = {}
        try:
            _country = c_m.Country.objects.get(pk=request.query_params['id'])
        except c_m.Country.DoesNotExist:
            return JsonResponse(
                {'result': 'The country does not exist'},
                )
        _country_serializer = c_s.CountrySerializer(
                _country, request.query_params
                )
        if _country_serializer.is_valid(raise_exception=True):
            _country_serializer.save()
            context['result'] = f'Country {request.query_params["name"]} was updated'
        else:
            context['result'] = 'error'
        return Response(context)

    def delete(self, request):
        context = {}
        try:
            _country = c_m.Country.objects.get(pk=request.query_params['id'])
        except c_m.Country.DoesNotExist:
            return JsonResponse(
                {'result': 'The country does not exist'},
                )
        _country.delete()
        context['result'] = f'Country {_country.name} was deleted'
        return Response(context)


class ManufacturerView(APIView):

    def get(self, request):
        context = {}
        try:
            _manufacturer_object = c_m.Manufacturer.objects.get(
                                            pk=request.query_params['id']
                                            )
        except c_m.Manufacturer.DoesNotExist:
            return JsonResponse(
                {'result': 'The manufacturer does not exist'},
                )
        _manufacturer = c_s.ManufacturerSerializer(
            _manufacturer_object
        ).data
        context['manufacturer'] = _manufacturer
        return Response(context)

    def post(self, request):
        context = {}
        _manufacturer_serializer = c_s.ManufacturerSerializer(
                                            data=request.query_params
                                            )
        if _manufacturer_serializer.is_valid(raise_exception=True):
            _manufacturer_serializer.save()
            context['result'] = f'Manufacturer {request.query_params["name"]} was created'
        else:
            context['result'] = 'error'
        return Response(context)

    def put(self, request):
        context = {}
        try:
            _manufacturer_object = c_m.Manufacturer.objects.get(
                                            pk=request.query_params['id']
                                            )
        except c_m.Manufacturer.DoesNotExist:
            return JsonResponse(
                {'result': 'The manufacturer does not exist'},
                )
        _manufacturer_serializer = c_s.ManufacturerSerializer(
                _manufacturer_object, request.query_params
                )
        if _manufacturer_serializer.is_valid(raise_exception=True):
            _manufacturer_serializer.save()
            context['result'] = f'Manufacturer {request.query_params["name"]} was updated'
        else:
            context['result'] = 'error'
        return Response(context)

    def delete(self, request):
        context = {}
        try:
            _manufacturer = c_m.Manufacturer.objects.get(pk=request.query_params['id'])
        except c_m.Manufacturer.DoesNotExist:
            return JsonResponse(
                {'result': 'The manufacturer does not exist'},
                )
        _manufacturer.delete()
        context['result'] = f'Manufacturer {_manufacturer.name} was deleted'
        return Response(context)


class VehicleView(APIView):

    def get(self, request):
        context = {}
        try:
            _vehicle_object = c_m.Vehicle.objects.get(
                                            pk=request.query_params['id']
                                            )
        except c_m.Vehicle.DoesNotExist:
            return JsonResponse(
                {'result': 'The manufacturer does not exist'},
                )
        _vehicle = c_s.VehicleSerializer(
            _vehicle_object
        ).data
        context['vehicle'] = _vehicle
        return Response(context)

    def post(self, request):
        context = {}
        _vehicle_serializer = c_s.VehicleSerializer(
                                            data=request.query_params
                                            )
        if _vehicle_serializer.is_valid(raise_exception=True):
            _vehicle_serializer.save()
            context['result'] = f'Vehicle {request.query_params["name"]} was created'
        else:
            context['result'] = 'error'
        return Response(context)

    def put(self, request):
        context = {}
        try:
            _vehicle_object = c_m.Vehicle.objects.get(
                                            pk=request.query_params['id']
                                            )
        except c_m.Vehicle.DoesNotExist:
            return JsonResponse(
                {'result': 'The vehicle does not exist'},
                )
        _vehicle_serializer = c_s.VehicleSerializer(
                _vehicle_object, request.query_params
                )
        if _vehicle_serializer.is_valid(raise_exception=True):
            _vehicle_serializer.save()
            context['result'] = f'Vehicle {request.query_params["name"]} was updated'
        else:
            context['result'] = 'error'
        return Response(context)

    def delete(self, request):
        context = {}
        try:
            _vehicle = c_m.Vehicle.objects.get(pk=request.query_params['id'])
        except c_m.Vehicle.DoesNotExist:
            return JsonResponse(
                {'result': 'The vehicle does not exist'},
                )
        _vehicle.delete()
        context['result'] = f'Vehicle {_vehicle.name} was deleted'
        return Response(context)


class CommentView(APIView):

    def get(self, request):
        context = {}
        try:
            _comment_object = c_m.Comment.objects.get(
                                            pk=request.query_params['id']
                                            )
        except c_m.Comment.DoesNotExist:
            return JsonResponse(
                {'result': 'The comment does not exist'},
                )
        _comment = c_s.CommentSerializer(
            _comment_object
        ).data
        context['comment'] = _comment
        return Response(context)

    def post(self, request):
        context = {}
        _comment_serializer = c_s.CommentSerializer(
                                            data=request.query_params
                                            )
        if _comment_serializer.is_valid(raise_exception=True):
            _comment_serializer.save()
            context['result'] = f'Comment from {request.query_params["author_email"]} was created'
        else:
            context['result'] = 'error'
        return Response(context)

    def put(self, request):
        context = {}
        try:
            _comment_object = c_m.Comment.objects.get(
                                            pk=request.query_params['id']
                                            )
        except c_m.Comment.DoesNotExist:
            return JsonResponse(
                {'result': 'The comment does not exist'},
                )
        _comment_serializer = c_s.CommentSerializer(
                _comment_object, request.query_params
                )
        if _comment_serializer.is_valid(raise_exception=True):
            _comment_serializer.save()
            context['result'] = f'Comment from {request.query_params["author_email"]} was updated'
        else:
            context['result'] = 'error'
        return Response(context)

    def delete(self, request):
        context = {}
        try:
            _comment_object = c_m.Comment.objects.get(pk=request.query_params['id'])
        except c_m.Comment.DoesNotExist:
            return JsonResponse(
                {'result': 'The comment does not exist'},
                )
        _comment_object.delete()
        context['result'] = f'Comment {request.query_params["id"]} was deleted'
        return Response(context)
