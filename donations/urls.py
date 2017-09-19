# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django import VERSION
from django.conf.urls import include, url

from donations.views import DonateAPI, VerifyAPI


def include_dj20(patterns, app_name, namespace):
    if VERSION < (1, 9):
        return include(patterns, namespace=namespace)
    else:
        return include((patterns, app_name), namespace=namespace)


app_name = 'donations'

api_urls = [
    url(r'^donate/$', DonateAPI.as_view(), name="donate"),
    url(r'^verify/(?P<pk>[0-9]+)$', VerifyAPI.as_view(), name="verify"),
]

donations = [
    url(r'^api/', include_dj20(api_urls, app_name='donations', namespace="api")),
]

urlpatterns = [
    url(r'^', include_dj20(donations, app_name='donations', namespace="donations"))
]
