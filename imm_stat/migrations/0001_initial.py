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
            name='ImmigrationProgram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('program_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ImmigrationStream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('stream_description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='ImmigrationSubProgram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('sub_program_description', models.CharField(max_length=2000)),
                ('program', models.ForeignKey(to='imm_stat.ImmigrationProgram')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
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
            name='UserStatisticFederalPhase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inland', models.BooleanField(default=False)),
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
                ('immigration_program', models.ForeignKey(to='imm_stat.ImmigrationProgram')),
                ('immigration_stream', models.ForeignKey(to='imm_stat.ImmigrationStream', null=True)),
                ('immigration_sub_program', models.ForeignKey(to='imm_stat.ImmigrationSubProgram', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserStatisticProvincialPhase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interview_location', models.CharField(max_length=200, null=True)),
                ('interview_date', models.DateField(null=True)),
                ('invitation_to_apply_date', models.DateField(null=True)),
                ('prov_file_date', models.DateField(null=True)),
                ('prov_request_additional_docs_date', models.DateField(null=True)),
                ('prov_nomination_date', models.DateField(null=True)),
                ('immigration_stream', models.ForeignKey(to='imm_stat.ImmigrationStream')),
                ('province', models.ForeignKey(to='imm_stat.Province')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='immigrationstream',
            name='province',
            field=models.ForeignKey(to='imm_stat.Province'),
        ),
    ]
