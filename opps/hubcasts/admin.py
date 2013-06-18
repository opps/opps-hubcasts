#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Streaming


class StreamingAdmin(admin.ModelAdmin):
    list_display = ['host', 'port', 'site', 'published']

    fieldsets = (
        (_(u'Identification'), {
            'fields': ('site', 'type', 'protocol', 'host', 'port')}),
        (_(u'Publication'), {
            'classes': ('extrapretty'),
            'fields': ('published', 'date_available')}),
    )


admin.site.register(Streaming, StreamingAdmin)
