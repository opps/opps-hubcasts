#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from opps.core.models import Publishable


class Streaming(Publishable):
    type = models.CharField(_(u'Type'), max_length=1, choices=(
        ('s', _(u'Shoutcast')), ('i', _(u'Icecast'))))
    protocol = models.CharField(_(u'Protocol'), max_length=5, choices=(
        ('http', _(u'HTTP')), ('https', _(u'HTTPS'))))
    host = models.CharField(_(u'Host IPV4'), max_length=16)
    port = models.PositiveIntegerField(verbose_name=_(u'Port TCP'),
                                       max_length=8)

    class Meta:
        verbose_name = _(u'Streaming')
        verbose_name_plural = _(u'Streaming')

    def get_absolute_url(self):
        return "/streaming/{}.asx".format(self.pk)
