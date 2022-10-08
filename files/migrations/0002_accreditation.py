# Generated by Django 4.0.2 on 2022-05-28 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
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
    ]