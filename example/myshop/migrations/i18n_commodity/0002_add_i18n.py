# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-22 12:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import filer.fields.image


def add_translation(apps, schema_editor):
    Commodity = apps.get_model('myshop', 'Commodity')
    Translation = apps.get_model('myshop', 'CommodityTranslation')
    for sc in Commodity.objects.all():
        for lang in settings.LANGUAGES:
            trans = Translation.objects.create(language_code=lang[0], caption=sc.caption,
                                               slug=sc.slug, product_name=sc.product_name,
                                               master=sc)
            trans.save()


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommodityTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('product_name', models.CharField(max_length=255, verbose_name='Product Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('caption', djangocms_text_ckeditor.fields.HTMLField(blank=True, help_text='Short description for the catalog list view.', null=True, verbose_name='Caption')),
            ],
        ),
        migrations.AddField(
            model_name='commoditytranslation',
            name='master',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='myshop.Commodity'),
        ),
        migrations.AlterUniqueTogether(
            name='commoditytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.RunPython(add_translation),
        migrations.RemoveField(
            model_name='commodity',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='commodity',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='commodity',
            name='slug',
        ),
        migrations.AlterField(
            model_name='commodity',
            name='sample_image',
            field=filer.fields.image.FilerImageField(blank=True, help_text="Sample image used in the catalog's list view.", null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image', verbose_name='Sample Image'),
        ),
    ]
