# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.urls import re_path, include

from rest_framework_tus.urls import urlpatterns as rest_framework_tus_urls

urlpatterns = [
    re_path(r'^', include((rest_framework_tus_urls, 'rest_framework_tus'), namespace='rest_framework_tus')),
]
