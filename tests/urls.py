# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url

from donations.urls import urlpatterns as donations_urls, include_dj20
from tests.views import SimpleDonateView, FixedDonateView, DonateThankYouView

test_app_urls = [
    url(r'^$', SimpleDonateView.as_view(), name='index'),
    url(r'^fixed/$', FixedDonateView.as_view(), name='fixed'),
    url(r'^thank-you/$', DonateThankYouView.as_view(), name='thank-you')
]

urlpatterns = [
    url(r'^', include_dj20(donations_urls, app_name='donations', namespace='donations')),
    url(r'^', include_dj20(test_app_urls, app_name='test-app', namespace="testapp")),
]
