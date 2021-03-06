# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 02:37
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('group_type', models.CharField(choices=[('ACTIVE DIRECTORY', 'Active Directory'), ('SOCIAL GROUP', 'Social Group'), ('PROJECT', 'Project'), ('WORKING GROUP', 'Working Group'), ('TEAM', 'Team'), ('GENERIC', 'Generic Group'), ('ORGANISATION', 'Organisation'), ('DISTRIBUTION LIST', 'Distribution List'), ('GOOGLE APPS', 'Google Apps Group')], default='GENERIC', max_length=20, verbose_name='Group Type')),
                ('google_group_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('ldap_group_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_group', to='organize.Group')),
            ],
            options={
                'ordering': ['name', 'group_type'],
            },
        ),
        migrations.CreateModel(
            name='GroupIdentifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('identifier', models.CharField(max_length=500)),
                ('identifier_type', models.CharField(choices=[('EMAIL', 'Email Address'), ('SKYPE', 'Skype ID'), ('IPADD', 'IP Address'), ('UNAME', 'Username'), ('TWITTER', 'Twitter ID'), ('NAME', 'Other name'), ('GOOGLE_ID', 'Google ID'), ('GUID', 'Guid'), ('SID', 'Sid')], default='EMAIL', max_length=10, verbose_name='Identifier Type')),
                ('primary_identifier', models.BooleanField(default=False)),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_ids', to='organize.Group')),
            ],
            options={
                'ordering': ['identifier', 'identifier_type'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupIdentifierAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ignore_type', models.IntegerField(choices=[(0, "Don't Ignore"), (1, 'Invalid Identifier')], default=0)),
                ('identifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organize.GroupIdentifier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z', 32), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('surname', models.CharField(blank=True, max_length=75, null=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z', 32), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')])),
                ('google_identity_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='Google Data')),
                ('ldap_identity_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='LDAP Data')),
                ('groups', models.ManyToManyField(blank=True, related_name='members', to='organize.Group')),
            ],
            options={
                'verbose_name': 'person',
                'ordering': ['surname', 'first_name'],
                'verbose_name_plural': 'people',
            },
        ),
        migrations.CreateModel(
            name='PersonAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('non_human', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organize.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonIdentifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('identifier', models.CharField(max_length=500)),
                ('identifier_type', models.CharField(choices=[('EMAIL', 'Email Address'), ('SKYPE', 'Skype ID'), ('IPADD', 'IP Address'), ('UNAME', 'Username'), ('TWITTER', 'Twitter ID'), ('NAME', 'Other name'), ('GOOGLE_ID', 'Google ID'), ('GUID', 'Guid'), ('SID', 'Sid')], default='EMAIL', max_length=10, verbose_name='Identifier Type')),
                ('primary_identifier', models.BooleanField(default=False)),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_ids', to='organize.Person')),
            ],
            options={
                'ordering': ['identifier', 'identifier_type'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonIdentifierAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ignore_type', models.IntegerField(choices=[(0, "Don't Ignore"), (1, 'Internal System Identifier'), (2, 'Personal Identifier')], default=0)),
                ('identifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organize.PersonIdentifier')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
