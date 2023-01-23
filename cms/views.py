from django.shortcuts import render

# Create your views here.

import cms.models as c_m


def country(request, country_id):
    context = {}
    _country = c_m.Country.objects.get(pk=country_id)
    context['country'] = _country
    context['manufacturer_list'] = c_m.Manufacturer.objects.filter(country=_country)
    return render(request, 'cms/country.html', context)


def index(request):
    context = {}
    context['country_list'] = c_m.Country.objects.all()
    return render(request, 'cms/index.html', context)