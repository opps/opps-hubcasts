#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mimetypes

from django.views.generic.detail import DetailView

from .models import Streaming


class StreamingPlay(DetailView):
    model = Streaming

    def render_to_response(self, context, **response_kwargs):
        self.ext = self.request.path.split('.')[1]

        context['host'] = self.object.host
        context['port'] = self.object.port
        context['protocol'] = self.object.protocol
        context['sufix'] = self.object.sufix
        context['site'] = self.object.site
        context['get_absolute_http'] = self.object.get_absolute_http

        response_kwargs['content_type'] = mimetypes.guess_type(
            'hubcasts/file.{}'.format(self.ext))[0]
        return super(StreamingPlay, self).render_to_response(
            context, mimetype=response_kwargs['content_type'],
            **response_kwargs)

    def get_template_names(self):
        return ['hubcasts/file.{}'.format(self.ext)]
