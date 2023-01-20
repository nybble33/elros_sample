# -*- coding: utf-8 -*-

from django.urls import path
from django.conf.urls import url

import api.views as a_v


urlpatterns = [
    path(r'country/', a_v.country),
]