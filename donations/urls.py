# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

from .views import DonateAPI, VerifyAPI

api_urls = [
    url(r'^donate/$', DonateAPI.as_view(), name="donate"),
    url(r'^verify/(?P<pk>[0-9]+)$', VerifyAPI.as_view(), name="verify"),
]

donations = [
    url(r'^api/', include(api_urls, namespace="api")),
]

urlpatterns = [
    url(r'^', include(donations, namespace="donations"))
]
