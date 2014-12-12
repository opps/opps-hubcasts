# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Streaming.mobile_type'
        db.add_column(u'hubcasts_streaming', 'mobile_type',
                      self.gf('django.db.models.fields.CharField')(default='o', max_length=1, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Streaming.mobile_protocol'
        db.add_column(u'hubcasts_streaming', 'mobile_protocol',
                      self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Streaming.mobile_host'
        db.add_column(u'hubcasts_streaming', 'mobile_host',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Streaming.mobile_port'
        db.add_column(u'hubcasts_streaming', 'mobile_port',
                      self.gf('django.db.models.fields.PositiveIntegerField')(max_length=8, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Streaming.mobile_sufix'
        db.add_column(u'hubcasts_streaming', 'mobile_sufix',
                      self.gf('django.db.models.fields.CharField')(max_length=155, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Streaming.mobile_type'
        db.delete_column(u'hubcasts_streaming', 'mobile_type')

        # Deleting field 'Streaming.mobile_protocol'
        db.delete_column(u'hubcasts_streaming', 'mobile_protocol')

        # Deleting field 'Streaming.mobile_host'
        db.delete_column(u'hubcasts_streaming', 'mobile_host')

        # Deleting field 'Streaming.mobile_port'
        db.delete_column(u'hubcasts_streaming', 'mobile_port')

        # Deleting field 'Streaming.mobile_sufix'
        db.delete_column(u'hubcasts_streaming', 'mobile_sufix')


    models = {
        u'%s.%s' % (User._meta.app_label, User._meta.module_name): {
            'Meta': {'object_name': User.__name__},
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hubcasts.streaming': {
            'Meta': {'object_name': 'Streaming'},
            'content': ('django.db.models.fields.CharField', [], {'default': "'audio'", 'max_length': '100'}),
            'date_available': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'db_index': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mirror_site': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'hubcasts_streaming_mirror_site'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['sites.Site']"}),
            'mobile_host': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mobile_port': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'mobile_protocol': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'mobile_sufix': ('django.db.models.fields.CharField', [], {'max_length': '155', 'null': 'True', 'blank': 'True'}),
            'mobile_type': ('django.db.models.fields.CharField', [], {'default': "'o'", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'port': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'protocol': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'site_domain': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'site_iid': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'sufix': ('django.db.models.fields.CharField', [], {'max_length': '155', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'o'", 'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s.%s']" % (User._meta.app_label, User._meta.object_name)})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['hubcasts']