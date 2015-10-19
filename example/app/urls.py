# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from .views import ExampleDonateView, ExampleThankYouView, ExampleFixedDonateView

urlpatterns = [
    url(r'^$', ExampleDonateView.as_view(), name='index'),
    url(r'^fixed/$', ExampleFixedDonateView.as_view(), name='fixed'),
    url(r'^thank-you/$', ExampleThankYouView.as_view(), name='thank-you')
]
