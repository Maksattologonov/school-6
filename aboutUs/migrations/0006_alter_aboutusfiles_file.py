# Generated by Django 4.0.2 on 2022-03-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutUs', '0005_alter_gloryboard_class_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutusfiles',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y/%m', verbose_name='Файл жүктөө'),
        ),
    ]
