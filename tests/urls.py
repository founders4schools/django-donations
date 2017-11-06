# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from donations.urls import urlpatterns as donations_urls
from tests.views import SimpleDonateView, FixedDonateView, DonateThankYouView

test_app_urls = [
    url(r'^$', SimpleDonateView.as_view(), name='index'),
    url(r'^fixed/$', FixedDonateView.as_view(), name='fixed'),
    url(r'^thank-you/$', DonateThankYouView.as_view(), name='thank-you')
]

urlpatterns = [
    url(r'^', include(donations_urls)),
    url(r'^', include(test_app_urls, namespace="testapp")),
]
