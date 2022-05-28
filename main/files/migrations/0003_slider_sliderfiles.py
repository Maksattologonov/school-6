# Generated by Django 4.0.2 on 2022-03-12 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_schedule_file_delete_schedulefiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Слайдердин тематикасы')),
            ],
            options={
                'verbose_name': 'Слайдер үчүн сүрөттөр',
                'verbose_name_plural': 'Слайдерлер сүрөттөрү',
                'db_table': 'slider',
            },
        ),
        migrations.CreateModel(
            name='SliderFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='files/%Y/%m', verbose_name='Сүрөт жүктөө')),
                ('slider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slider_images', to='files.slider')),
            ],
            options={
                'db_table': 'sliders_files',
            },
        ),
    ]