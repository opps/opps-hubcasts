#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from piston.resource import Resource

from .api import StreamingHandler


streaming = Resource(handler=StreamingHandler)

urlpatterns = patterns(
    '',
    url(r'^api/hubcasts/$', streaming, {'emitter_format': 'json'}),
)
