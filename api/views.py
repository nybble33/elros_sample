from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse

import cms.serializers as c_s
import cms.models as c_m


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def country(request):
    context = {'method': request.method}
    if request.method == 'GET':
        _country = c_s.CountrySerializer(
            c_m.Country.objects.get(pk=request.GET['id'])
        ).data
        context['country'] = _country
    return JsonResponse(context)