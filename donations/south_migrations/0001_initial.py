# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Frequency'
        db.create_table('donations_frequency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('interval', self.gf('timedelta.fields.TimedeltaField')()),
        ))
        db.send_create_signal('donations', ['Frequency'])

        # Adding model 'DonationProvider'
        db.create_table('donations_donationprovider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='BlankProvider', max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('klass', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal('donations', ['DonationProvider'])

        # Adding model 'Donation'
        db.create_table('donations_donation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount_currency', self.gf('djmoney.models.fields.CurrencyField')(default='GBP')),
            ('amount', self.gf('djmoney.models.fields.MoneyField')(max_digits=10, decimal_places=2, default_currency='GBP')),
            ('provider', self.gf('django.db.models.fields.related.ForeignKey')(related_name='donations', to=orm['donations.DonationProvider'])),
            ('frequency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='donations', to=orm['donations.Frequency'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('donor', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='donations', null=True, to=orm['auth.User'])),
            ('donor_display_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='Unverified', max_length=50)),
            ('is_verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('finished_uri', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('provider_ref', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('local_amount_currency', self.gf('djmoney.models.fields.CurrencyField')(default='GBP')),
            ('local_amount', self.gf('djmoney.models.fields.MoneyField')(max_digits=10, decimal_places=2, default_currency='GBP')),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('est_tax_reclaim', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('provider_source', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('donations', ['Donation'])


    def backwards(self, orm):
        # Deleting model 'Frequency'
        db.delete_table('donations_frequency')

        # Deleting model 'DonationProvider'
        db.delete_table('donations_donationprovider')

        # Deleting model 'Donation'
        db.delete_table('donations_donation')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'donations.donation': {
            'Meta': {'object_name': 'Donation'},
            'amount': ('djmoney.models.fields.MoneyField', [], {'max_digits': '10', 'decimal_places': '2', 'default_currency': "'GBP'"}),
            'amount_currency': ('djmoney.models.fields.CurrencyField', [], {'default': "'GBP'"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'donor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'donations'", 'null': 'True', 'to': "orm['auth.User']"}),
            'donor_display_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'est_tax_reclaim': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'finished_uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'frequency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'donations'", 'to': "orm['donations.Frequency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'local_amount': ('djmoney.models.fields.MoneyField', [], {'max_digits': '10', 'decimal_places': '2', 'default_currency': "'GBP'"}),
            'local_amount_currency': ('djmoney.models.fields.CurrencyField', [], {'default': "'GBP'"}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'donations'", 'to': "orm['donations.DonationProvider']"}),
            'provider_ref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'provider_source': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Unverified'", 'max_length': '50'})
        },
        'donations.donationprovider': {
            'Meta': {'object_name': 'DonationProvider'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'BlankProvider'", 'max_length': '100'})
        },
        'donations.frequency': {
            'Meta': {'object_name': 'Frequency'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interval': ('timedelta.fields.TimedeltaField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['donations']
