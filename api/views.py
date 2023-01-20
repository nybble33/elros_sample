from django.shortcuts import render

# Create your views here.

# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

import cms.serializers as c_s
import cms.models as c_m

class CountryView(APIView):
    def get(self, request):
        context = {}
        _country = c_s.CountrySerializer(
            c_m.Country.objects.get(pk=request.GET['id'])
        ).data
        context['country'] = _country