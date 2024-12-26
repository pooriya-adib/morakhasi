# Generated by Django 5.1.4 on 2024-12-25 07:54

import django.core.validators
import django.db.models.deletion
import django_jalali.db.models
import jdatetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nation_code', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='کد ملی')),
                ('name', models.CharField(max_length=255, verbose_name='نام')),
                ('family', models.CharField(max_length=255, verbose_name='نام خانوادگی')),
                ('father_name', models.CharField(max_length=255, verbose_name='نام پدر')),
                ('mobile_number', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='تلفن همراه')),
                ('car', models.CharField(max_length=255, verbose_name='سیستم')),
                ('city_code', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='ایران')),
                ('three_len_code', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='سه رقم')),
                ('alphabet', models.CharField(max_length=1, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='حرف')),
                ('two_len_code', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='دو رقم')),
                ('leave_restriction', models.IntegerField(default=0, verbose_name='مرخصی های باقی مانده')),
            ],
            options={
                'verbose_name': 'راننده مد نظر',
                'verbose_name_plural': 'راننده ها',
            },
        ),
        migrations.CreateModel(
            name='LeaveRestriction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_per_year', models.IntegerField(default=60, verbose_name='تعداد روز های مجاز سالانه')),
            ],
            options={
                'verbose_name': 'تعداد روز های مجاز مرخصی سالانه',
                'verbose_name_plural': 'مرخصی در سال',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='اسم استان')),
            ],
            options={
                'verbose_name': 'استان مد نظر',
                'verbose_name_plural': 'استان ها',
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nation_code', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='کد ملی')),
                ('mobile_number', models.CharField(max_length=14, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='شماره تماس')),
                ('start_date', django_jalali.db.models.jDateField(default=jdatetime.date.today, verbose_name='شروع مرخصی')),
                ('end_date', django_jalali.db.models.jDateField(default=jdatetime.date.today, verbose_name='پایان مرخصی')),
                ('state_origin_trip', models.CharField(default='مازندران', max_length=250, verbose_name='استان مبدا سفر راننده')),
                ('city_origin_trip', models.CharField(default='آمل', max_length=250, verbose_name='شهر مبدا سفر راننده')),
                ('state_travel_destination', models.CharField(default='', max_length=250, verbose_name='استان مقصد سفر راننده')),
                ('city_travel_destination', models.CharField(default='', max_length=250, verbose_name='شهر مقصد سفر راننده')),
                ('status', models.BooleanField(default=False, verbose_name='تایید فرم مرخصی راننده')),
                ('driver', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='leave.driver')),
            ],
            options={
                'verbose_name': 'فرم مرخصی',
                'verbose_name_plural': 'فرم مرخصی ها',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='شهر استان')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave.state', verbose_name='اسم استان مربوط')),
            ],
            options={
                'verbose_name': 'شهر مد نظر',
                'verbose_name_plural': 'شهر ها',
            },
        ),
    ]
