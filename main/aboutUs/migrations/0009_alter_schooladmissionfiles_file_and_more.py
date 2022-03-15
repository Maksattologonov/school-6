# Generated by Django 4.0.2 on 2022-03-15 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutUs', '0008_schooladmissionfiles_school_admin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooladmissionfiles',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y/%m', verbose_name='Файл жүктөө'),
        ),
        migrations.AlterField(
            model_name='schooladmissionfiles',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Аталышы'),
        ),
    ]
