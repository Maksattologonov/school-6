# Generated by Django 4.0.2 on 2022-03-02 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            name='ScheduleFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Файл жөнүндө маалымат')),
                ('file', models.FileField(null=True, upload_to='files/%Y/%m', verbose_name='Файл жүктөө')),
                ('about_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_files', to='files.schedule')),
            ],
            options={
                'db_table': 'schedule_files',
            },
        ),
        migrations.CreateModel(
            name='GalleryFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Сүрөт жөнүндө маалымат')),
                ('file', models.ImageField(null=True, upload_to='files/%Y/%m', verbose_name='Сүрөт жүктөө')),
                ('about_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_files', to='files.gallery')),
            ],
            options={
                'db_table': 'gallery_files',
            },
        ),
    ]