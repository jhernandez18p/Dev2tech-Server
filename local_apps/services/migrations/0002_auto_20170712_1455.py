# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 19:55
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='beneficios',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='benefits',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='context',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='en_checklist',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='es_checklist',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='eslogan',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='objectives',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='objetivos',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='proceso',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='process',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='projects',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='related',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='slogan',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='technology',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='tecnologia',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
