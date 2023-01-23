# -*- coding: utf-8 -*-

from django.urls import path

import api.views as a_v


urlpatterns = [
    path(r'country/', a_v.CountryView.as_view()),
    path(r'manufacturer/', a_v.ManufacturerView.as_view()),
    path(r'vehicle/', a_v.VehicleView.as_view()),
    path(r'comment/', a_v.CommentView.as_view()),
]