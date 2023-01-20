# -*- coding: utf-8 -*-

from django.conf.urls import url

import cms.views as c_v


urlpatterns = [
    url(r'^$', c_v.index),
    ]
