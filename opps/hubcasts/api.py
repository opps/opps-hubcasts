#!/usr/bin/env python
# -*- coding: utf-8 -*-
from opps.api import BaseHandler

from .models import Streaming


class StreamingHandler(BaseHandler):
    model = Streaming
