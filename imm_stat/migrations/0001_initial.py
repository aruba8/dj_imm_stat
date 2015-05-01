# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserStatistic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(null=True)),
                ('username', models.CharField(max_length=80)),
                ('stream', models.CharField(max_length=80, null=True)),
                ('from_country', django_countries.fields.CountryField(max_length=2)),
                ('interview_location', models.CharField(max_length=200, null=True)),
                ('interview_date', models.DateTimeField(null=True)),
                ('invitation_to_apply_date', models.DateTimeField(null=True)),
                ('mpnp_file_date', models.DateTimeField(null=True)),
                ('mpnp_request_additional_docs_date', models.DateTimeField(null=True)),
                ('mpnp_nomination_date', models.DateTimeField(null=True)),
                ('cio_received_date', models.DateTimeField(null=True)),
                ('cio_processing_fee_date', models.DateTimeField(null=True)),
                ('cio_file_number', models.DateTimeField(null=True)),
                ('embassy', models.CharField(max_length=80, null=True)),
                ('ecas_recieved', models.DateTimeField(null=True)),
                ('ecas_in_process', models.DateTimeField(null=True)),
                ('ecas_additional_documents_request1', models.DateTimeField(null=True)),
                ('ecas_medical_forms', models.DateTimeField(null=True)),
                ('ecas_medical_exam_passed', models.DateTimeField(null=True)),
                ('ecas_medical_results_received', models.DateTimeField(null=True)),
                ('ecas_additional_documents_request2', models.DateTimeField(null=True)),
                ('povl_date', models.DateTimeField(null=True)),
            ],
        ),
    ]
