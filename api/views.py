from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def country(request):
    context = {'method': request.method}
    return JsonResponse(context)