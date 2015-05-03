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
            name='ProvincialStream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stream', models.CharField(default=b'MBG', max_length=3, choices=[(b'MBG', b'Manitoba MPNP general stream'), (b'MBS', b'Manitoba MPNP strategic stream')])),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stream', models.CharField(default=b'EE', max_length=2, choices=[(b'EE', b'Skilled immigrants (Express Entry)'), (b'QE', b'Quebec-selected skilled workers (or investor or entrepreneur program)'), (b'SU', b'Start-up visa'), (b'II', b'Immigrant Investor Venture Capital Pilot Program'), (b'SE', b'Self-employed Persons Program'), (b'FS', b'Family sponsorship'), (b'PN', b'Provincial nominees'), (b'CR', b'Caregivers'), (b'RF', b'Refugees')])),
            ],
        ),
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
                ('stream', models.CharField(max_length=2, null=True, choices=[(b'EE', b'Skilled immigrants (Express Entry)'), (b'QE', b'Quebec-selected skilled workers (or investor or entrepreneur program)'), (b'SU', b'Start-up visa'), (b'II', b'Immigrant Investor Venture Capital Pilot Program'), (b'SE', b'Self-employed Persons Program'), (b'FS', b'Family sponsorship'), (b'PN', b'Provincial nominees'), (b'CR', b'Caregivers'), (b'RF', b'Refugees')])),
                ('provincial_stream', models.CharField(max_length=80, null=True, choices=[(b'MBG', b'Manitoba MPNP general stream'), (b'MBS', b'Manitoba MPNP strategic stream')])),
                ('from_country', django_countries.fields.CountryField(max_length=2)),
                ('interview_location', models.CharField(max_length=200, null=True)),
                ('interview_date', models.DateField(null=True)),
                ('invitation_to_apply_date', models.DateField(null=True)),
                ('mpnp_file_date', models.DateField(null=True)),
                ('mpnp_request_additional_docs_date', models.DateField(null=True)),
                ('mpnp_nomination_date', models.DateField(null=True)),
                ('cio_received_date', models.DateField(null=True)),
                ('cio_processing_fee_date', models.DateField(null=True)),
                ('cio_file_number', models.DateField(null=True)),
                ('embassy', models.CharField(max_length=80, null=True)),
                ('ecas_recieved', models.DateField(null=True)),
                ('ecas_in_process', models.DateField(null=True)),
                ('ecas_additional_documents_request1', models.DateField(null=True)),
                ('ecas_medical_forms', models.DateField(null=True)),
                ('ecas_medical_exam_passed', models.DateField(null=True)),
                ('ecas_medical_results_received', models.DateField(null=True)),
                ('ecas_additional_documents_request2', models.DateField(null=True)),
                ('povl_date', models.DateField(null=True)),
            ],
        ),
    ]
