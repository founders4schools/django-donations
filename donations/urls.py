# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url, patterns
from .views import DonateAPI, VerifyAPI


urlpatterns = patterns(
    '',
    url(r'^donate/$', DonateAPI.as_view(), name="donate"),
    url(r'^verify/(?P<id>[0-9]+)$', VerifyAPI.as_view(), name="verify"),
)
