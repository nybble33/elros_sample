# -*- coding: utf-8 -*-

from django.conf.urls import url

import cms.views as c_v


urlpatterns = [
    url(r'^$', c_v.index),
    # `url(r'country/<int:country_id>/', c_v.country),
    url(r'country/(?P<country_id>[-\w]+)/', c_v.country),
    ]
