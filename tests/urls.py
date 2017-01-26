# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from donations.urls import urlpatterns as donations_urls

urlpatterns = [
    url(r'^', include(donations_urls, namespace='donations')),
]
