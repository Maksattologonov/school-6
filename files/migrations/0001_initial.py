# Generated by Django 3.2.9 on 2022-11-12 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accreditation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Аккредитация документтери')),
                ('file', models.FileField(null=True, upload_to='files/%Y/%m', verbose_name='Файл жүктөө')),
            ],
            options={
                'verbose_name': 'Аккредитация',
                'verbose_name_plural': 'Аккредитация',
                'db_table': 'accreditation',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Сүрөттүн тематикасы')),
            ],
            options={
                'verbose_name': 'Сүрөт',
                'verbose_name_plural': 'Галлерея',
                'db_table': 'gallery',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_no', models.CharField(max_length=255, verbose_name='Класстын расписаниеси')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
                'db_table': 'schedule',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Слайдердин аталышы')),
                ('file', models.FileField(null=True, upload_to='files/%Y/%m', verbose_name='Файл жүктөө')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдер',
                'db_table': 'slider',
            },
        ),
        migrations.CreateModel(
            name='ScheduleFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='files/%Y/%m', verbose_name='Файл жүктөө')),
                ('schedule_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedule_files', to='files.schedule')),
            ],
            options={
                'db_table': 'schedule_files',
            },
        ),
        migrations.CreateModel(
            name='GalleryFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(null=True, upload_to='files/%Y/%m', verbose_name='Сүрөт жүктөө')),
                ('gallery_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gallery_files', to='files.gallery')),
            ],
            options={
                'db_table': 'gallery_files',
            },
        ),
    ]
