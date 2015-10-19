# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url, patterns
from .views import DonateAPI, VerifyAPI

api_urls = patterns(
    '',
    url(r'^donate/$', DonateAPI.as_view(), name="donate"),
    url(r'^verify/(?P<pk>[0-9]+)$', VerifyAPI.as_view(), name="verify"),
)

view_urls = patterns(
    '',
    # url(r'^donate/$', DonateView.as_view(), name="donate"),
)

donations = patterns(
    '',
    url(r'^api/', include(api_urls, namespace="api")),
    url(r'^', include(view_urls)),
)

urlpatterns = patterns(
    '',
    url(r'^', include(donations, namespace="donations"))
)
