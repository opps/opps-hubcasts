#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from opps.core.models import Publishable


class Streaming(Publishable):
    TYPES = (
        ('o', _(u'Other')),
        ('u', _(u'Direct URL')),
        ('s', _(u'Shoutcast')),
        ('i', _(u'Icecast')),
    )
    PROTOCOLS = (
        ('http', _(u'HTTP')),
        ('https', _(u'HTTPS')),
        ('rtmp', _(u'RTMP')),
        ('mms', _(u'MMS')),
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    type = models.CharField(
        _(u'Type'),
        max_length=1,
        choices=TYPES,
        default='o'
    )

    content_type = models.CharField(
        _(u'Content-Type'),
        max_length=50,
        blank=True,
        help_text='audio/mp3, audio/aac...'
    )

    protocol = models.CharField(
        _(u'Protocol'),
        max_length=5,
        choices=PROTOCOLS,
        null=True,
        blank=True
    )

    host = models.CharField(
        _(u'Hostname'),
        max_length=255,
        help_text=_(u'Hostname or full url')
    )

    port = models.PositiveIntegerField(
        verbose_name=_(u'Port TCP'),
        max_length=8,
        null=True,
        blank=True
    )

    sufix = models.CharField(
        verbose_name=_(u'Streaming sufix'),
        max_length=155,
        null=True,
        blank=True
    )

    mobile_type = models.CharField(
        _(u'Type'),
        max_length=1,
        choices=TYPES,
        default='o',
        null=True,
        blank=True
    )

    mobile_content_type = models.CharField(
        _(u'Content-Type'),
        max_length=50,
        blank=True,
        help_text='audio/mp3, audio/aac...'
    )

    mobile_protocol = models.CharField(
        _(u'Protocol'),
        max_length=5,
        choices=PROTOCOLS,
        null=True,
        blank=True
    )

    mobile_host = models.CharField(
        _(u'Hostname'),
        max_length=255,
        help_text=_(u'Hostname or full url'),
        null=True,
        blank=True
    )

    mobile_port = models.PositiveIntegerField(
        verbose_name=_(u'Port TCP'),
        max_length=8,
        null=True,
        blank=True
    )

    mobile_sufix = models.CharField(
        verbose_name=_(u'Streaming sufix'),
        max_length=155,
        null=True,
        blank=True
    )

    content = models.CharField(
        _('Content'),
        max_length=100,
        default='audio',
        choices=(
            ('audio', _('Audio')),
            ('video', _('Video')),
        )
    )

    class Meta:
        verbose_name = _(u'Streaming')
        verbose_name_plural = _(u'Streamings')

    def __unicode__(self):
        return self.get_absolute_url()

    def get_absolute_url(self):
        if self.type in ['o', 'u']:
            return self.get_absolute_http()
        return "/streaming/{}.asx".format(self.pk)

    def get_absolute_http(self):
        if self.type == 'u':
            return self.host
        host = "{}://{}".format(self.protocol, self.host)
        if self.port:
            host = "{}:{}".format(host, self.port)
        if self.sufix:
            host = "{}{}".format(host, self.sufix)
        return host

    def get_mobile_absolute_http(self):
        if self.mobile_type == 'u':
            return self.mobile_host
        mobile_host = "{}://{}".format(self.mobile_protocol, self.mobile_host)
        if self.mobile_port:
            mobile_host = "{}:{}".format(mobile_host, self.mobile_port)
        if self.mobile_sufix:
            mobile_host = "{}{}".format(mobile_host, self.mobile_sufix)
        return mobile_host
