#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.conf import settings
from django.views.decorators.cache import cache_page

from .views import StreamingPlay


urlpatterns = patterns(
    '',
    url(r'^(?P<pk>[\d]+).(asx|rm|pls)$',
        cache_page(settings.OPPS_CACHE_EXPIRE)(StreamingPlay.as_view()),
        name='blogpost-detail')
)
