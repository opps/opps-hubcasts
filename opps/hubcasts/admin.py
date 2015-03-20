#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils import timezone
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from opps.contrib.multisite.admin import AdminViewPermission
from opps.core.admin import PublishableAdmin
from .models import Streaming


class StreamingAdmin(PublishableAdmin, AdminViewPermission):
    list_display = ['title', 'host', 'url', 'port', 'sufix', 'site',
                    'type', 'content', 'published']

    list_filter = ['content', 'site', 'type', 'published']
    search_fields = ['name', 'host', 'content', 'site__domain']
    fieldsets = (
        (_(u'Identification'), {
            'fields': ('site', 'name', 'content')}),
        (_(u'Desktop'), {
            'fields': ('type', 'protocol', 'host',
                       'port', 'sufix', 'content_type',)}),
        (_(u'Mobile'), {
            'fields': ('mobile_type', 'mobile_protocol', 'mobile_host',
                       'mobile_port', 'mobile_sufix','mobile_content_type',)}),
        (_(u'Publication'), {
            'classes': ('extrapretty'),
            'fields': ('published', 'date_available')}),
    )

    def title(self, obj, *args, **kwargs):
        return obj.name or obj.host

    def url(self, obj, *args, **kwargs):
        return obj.get_absolute_url()

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'pk', None) is None:
            obj.user = get_user_model().objects.get(pk=request.user.pk)
            obj.date_insert = timezone.now()
            obj.site = Site.objects.get(pk=settings.SITE_ID)
        obj.date_update = timezone.now()
        obj.save()


admin.site.register(Streaming, StreamingAdmin)
