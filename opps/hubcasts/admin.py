#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils import timezone
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
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

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'pk', None) is None:
            obj.user = get_user_model().objects.get(pk=request.user.pk)
            obj.date_insert = timezone.now()
            obj.site = Site.objects.get(pk=settings.SITE_ID)
        obj.date_update = timezone.now()
        obj.save()


admin.site.register(Streaming, StreamingAdmin)
