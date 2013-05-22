# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Proyecto'
        db.create_table('contraparte_proyecto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trocaire.Organizacion'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('inicio', self.gf('django.db.models.fields.DateField')()),
            ('finalizacion', self.gf('django.db.models.fields.DateField')()),
            ('monto_trocaire', self.gf('django.db.models.fields.IntegerField')()),
            ('monto_contrapartida', self.gf('django.db.models.fields.IntegerField')()),
            ('contacto', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('aporta_trocaire', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('contraparte', ['Proyecto'])

        # Adding M2M table for field municipios on 'Proyecto'
        db.create_table('contraparte_proyecto_municipios', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyecto', models.ForeignKey(orm['contraparte.proyecto'], null=False)),
            ('municipio', models.ForeignKey(orm['lugar.municipio'], null=False))
        ))
        db.create_unique('contraparte_proyecto_municipios', ['proyecto_id', 'municipio_id'])

        # Adding model 'Resultado'
        db.create_table('contraparte_resultado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_corto', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('aporta_a', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trocaire.ResultadoPrograma'])),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contraparte.Proyecto'])),
        ))
        db.send_create_signal('contraparte', ['Resultado'])

        # Adding model 'Organizador'
        db.create_table('contraparte_organizador', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('contraparte', ['Organizador'])

        # Adding model 'Actividad'
        db.create_table('contraparte_actividad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trocaire.Organizacion'])),
            ('proyecto', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['contraparte.Proyecto'])),
            ('persona_organiza', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contraparte.Organizador'])),
            ('nombre_actividad', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
            ('municipio', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Municipio'])),
            ('comunidad', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Comunidad'])),
            ('tipo_actividad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trocaire.TipoActividad'])),
            ('tema_actividad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trocaire.Tema'])),
            ('ejes_transversales', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trocaire.EjeTransversal'])),
            ('hombres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('no_dato', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('adultos', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('jovenes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ninos', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('no_dato1', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('autoridades', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('maestros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('lideres', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pobladores', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('estudiantes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('miembros', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('tecnicos', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('resultado', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['contraparte.Resultado'])),
            ('relevancia', self.gf('django.db.models.fields.IntegerField')()),
            ('efectividad', self.gf('django.db.models.fields.IntegerField')()),
            ('aprendizaje', self.gf('django.db.models.fields.IntegerField')()),
            ('empoderamiento', self.gf('django.db.models.fields.IntegerField')()),
            ('participacion', self.gf('django.db.models.fields.IntegerField')()),
            ('relevancia_m', self.gf('django.db.models.fields.IntegerField')()),
            ('efectividad_m', self.gf('django.db.models.fields.IntegerField')()),
            ('aprendizaje_m', self.gf('django.db.models.fields.IntegerField')()),
            ('empoderamiento_m', self.gf('django.db.models.fields.IntegerField')()),
            ('participacion_m', self.gf('django.db.models.fields.IntegerField')()),
            ('comentarios', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('acuerdos', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('foto1', self.gf('g12d.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True)),
            ('foto2', self.gf('g12d.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True)),
            ('foto3', self.gf('g12d.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True)),
            ('video', self.gf('django.db.models.fields.CharField')(default='', max_length=300, blank=True)),
            ('mes', self.gf('django.db.models.fields.IntegerField')()),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('contraparte', ['Actividad'])

        # Adding model 'Output'
        db.create_table('contraparte_output', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('params', self.gf('django.db.models.fields.TextField')()),
            ('comment', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('file', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bar_img', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('pie1_img', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('pie2_img', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('html_table', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('bar_chart', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('pie_chart_one', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('pie_chart_two', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('contraparte', ['Output'])


    def backwards(self, orm):
        # Deleting model 'Proyecto'
        db.delete_table('contraparte_proyecto')

        # Removing M2M table for field municipios on 'Proyecto'
        db.delete_table('contraparte_proyecto_municipios')

        # Deleting model 'Resultado'
        db.delete_table('contraparte_resultado')

        # Deleting model 'Organizador'
        db.delete_table('contraparte_organizador')

        # Deleting model 'Actividad'
        db.delete_table('contraparte_actividad')

        # Deleting model 'Output'
        db.delete_table('contraparte_output')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'contraparte.actividad': {
            'Meta': {'object_name': 'Actividad'},
            'acuerdos': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'adultos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'aprendizaje': ('django.db.models.fields.IntegerField', [], {}),
            'aprendizaje_m': ('django.db.models.fields.IntegerField', [], {}),
            'autoridades': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'comentarios': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'comunidad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'efectividad': ('django.db.models.fields.IntegerField', [], {}),
            'efectividad_m': ('django.db.models.fields.IntegerField', [], {}),
            'ejes_transversales': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trocaire.EjeTransversal']"}),
            'empoderamiento': ('django.db.models.fields.IntegerField', [], {}),
            'empoderamiento_m': ('django.db.models.fields.IntegerField', [], {}),
            'estudiantes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'foto1': ('g12d.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto2': ('g12d.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'foto3': ('g12d.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'hombres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jovenes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lideres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'maestros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mes': ('django.db.models.fields.IntegerField', [], {}),
            'miembros': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'ninos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'no_dato': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'no_dato1': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nombre_actividad': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trocaire.Organizacion']"}),
            'participacion': ('django.db.models.fields.IntegerField', [], {}),
            'participacion_m': ('django.db.models.fields.IntegerField', [], {}),
            'persona_organiza': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Organizador']"}),
            'pobladores': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'proyecto': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['contraparte.Proyecto']"}),
            'relevancia': ('django.db.models.fields.IntegerField', [], {}),
            'relevancia_m': ('django.db.models.fields.IntegerField', [], {}),
            'resultado': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['contraparte.Resultado']"}),
            'tecnicos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tema_actividad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trocaire.Tema']"}),
            'tipo_actividad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trocaire.TipoActividad']"}),
            'video': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'contraparte.organizador': {
            'Meta': {'object_name': 'Organizador'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'contraparte.output': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Output'},
            'bar_chart': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'bar_img': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'file': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'html_table': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'params': ('django.db.models.fields.TextField', [], {}),
            'pie1_img': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pie2_img': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pie_chart_one': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'pie_chart_two': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'contraparte.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'aporta_trocaire': ('django.db.models.fields.IntegerField', [], {}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'finalizacion': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio': ('django.db.models.fields.DateField', [], {}),
            'monto_contrapartida': ('django.db.models.fields.IntegerField', [], {}),
            'monto_trocaire': ('django.db.models.fields.IntegerField', [], {}),
            'municipios': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lugar.Municipio']", 'symmetrical': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trocaire.Organizacion']"})
        },
        'contraparte.resultado': {
            'Meta': {'object_name': 'Resultado'},
            'aporta_a': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trocaire.ResultadoPrograma']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Proyecto']"})
        },
        'lugar.comunidad': {
            'Meta': {'object_name': 'Comunidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'trocaire.ejetransversal': {
            'Meta': {'object_name': 'EjeTransversal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'trocaire.organizacion': {
            'Meta': {'object_name': 'Organizacion'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'contacto': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'direccion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'blank': 'True'}),
            'historia': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_register': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 21, 0, 0)'}),
            'logo': ('g12d.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '12', 'blank': 'True'}),
            'web': ('django.db.models.fields.URLField', [], {'default': "'www.example.com'", 'max_length': '200', 'blank': 'True'})
        },
        'trocaire.resultadoprograma': {
            'Meta': {'object_name': 'ResultadoPrograma'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'trocaire.tema': {
            'Meta': {'object_name': 'Tema'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'trocaire.tipoactividad': {
            'Meta': {'object_name': 'TipoActividad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['contraparte']