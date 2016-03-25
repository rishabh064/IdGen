# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-24 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('dateofbirth', models.DateField()),
                ('bloodgroup', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=10)),
                ('photo', models.ImageField(upload_to='faculty')),
            ],
        ),
        migrations.CreateModel(
            name='FDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=120)),
                ('cfont', models.CharField(max_length=120)),
                ('cfontsize', models.IntegerField()),
                ('addline1', models.CharField(max_length=120)),
                ('addline1font', models.CharField(max_length=120)),
                ('addline1fontsize', models.IntegerField()),
                ('addline2', models.CharField(max_length=120)),
                ('addline3', models.CharField(max_length=120)),
                ('addline4', models.CharField(max_length=120)),
                ('addline5', models.CharField(max_length=120)),
                ('addline2to5font', models.CharField(max_length=120)),
                ('addline2to5fontsize', models.IntegerField()),
                ('detfont', models.CharField(max_length=120)),
                ('detfontsize', models.IntegerField()),
                ('ilogo', models.ImageField(blank=True, null=True, upload_to='template_faculty')),
                ('psign', models.ImageField(blank=True, null=True, upload_to='template_faculty')),
                ('bdesign', models.ImageField(blank=True, null=True, upload_to='template_faculty')),
            ],
        ),
        migrations.CreateModel(
            name='SDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=120)),
                ('cfont', models.CharField(max_length=120)),
                ('cfontsize', models.IntegerField()),
                ('addline1', models.CharField(max_length=120)),
                ('addline2', models.CharField(max_length=120)),
                ('addline3', models.CharField(max_length=120)),
                ('addline4', models.CharField(max_length=120)),
                ('addline5', models.CharField(max_length=120)),
                ('addline1to5font', models.CharField(max_length=120)),
                ('addline1to5fontsize', models.IntegerField()),
                ('detfont', models.CharField(max_length=120)),
                ('detfontsize', models.IntegerField()),
                ('clogo', models.ImageField(blank=True, null=True, upload_to='template_student')),
                ('ilogo', models.ImageField(blank=True, null=True, upload_to='template_student')),
                ('psign', models.ImageField(blank=True, null=True, upload_to='template_student')),
                ('bdesign', models.ImageField(blank=True, null=True, upload_to='template_student')),
            ],
        ),
        migrations.CreateModel(
            name='stud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
                ('admno', models.CharField(max_length=200, unique=True)),
                ('validtill', models.DateField()),
                ('dateofbirth', models.DateField()),
                ('bloodgroup', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('contact1', models.CharField(max_length=10)),
                ('contact2', models.CharField(blank=True, max_length=10, null=True)),
                ('photo', models.ImageField(upload_to='student')),
                ('clss', models.CharField(blank=True, max_length=5, null=True)),
                ('rollno', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
    ]
