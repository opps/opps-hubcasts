#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from opps.core.models import Publishable


class Streaming(Publishable):
    type = models.CharField(_(u'Type'), max_length=1, choices=(
        ('s', _(u'Shoutcast')), ('i', _(u'Icecast')), ('o', _(u'Other'))))
    protocol = models.CharField(_(u'Protocol'), max_length=5, choices=(
        ('http', _(u'HTTP')),
        ('https', _(u'HTTPS')),
        ('rtmp', _(u'RTMP')),
        ('mms', _(u'MMS')),
    ),)
    host = models.CharField(_(u'Hostname'), max_length=50)
    port = models.PositiveIntegerField(verbose_name=_(u'Port TCP'),
                                       max_length=8, null=True, blank=True)
    sufix = models.CharField(verbose_name=_(u'Streaming sufix'),
                             max_length=155, null=True, blank=True)

    class Meta:
        verbose_name = _(u'Streaming')
        verbose_name_plural = _(u'Streamings')

    def __unicode__(self):
        return self.get_absolute_url()

    def get_absolute_url(self):
        if self.type == 'o':
            return self.get_absolute_http()
        return "/streaming/{}.asx".format(self.pk)

    def get_absolute_http(self):
        host = "{}://{}".format(self.protocol, self.host)
        if self.port:
            host = "{}:{}".format(host, self.port)
        if self.sufix:
            host = "{}{}".format(host, self.sufix)
        return host
