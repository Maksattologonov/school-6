# Generated by Django 4.0.2 on 2022-03-04 09:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Жаңылыктын темасы')),
                ('description', models.TextField(verbose_name='Жаңылыктын маалыматы')),
                ('created_at', models.DateField(default=django.utils.timezone.now, editable=False, verbose_name='Жазылган дата')),
            ],
            options={
                'verbose_name': 'Жаңылык',
                'verbose_name_plural': 'Жаңылыктар',
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Файл жөнүндө маалымат')),
                ('description', models.TextField(verbose_name='Жаңылыктын маалыматы')),
                ('created_at', models.DateField(default=django.utils.timezone.now, editable=False, verbose_name='Жазылган дата')),
                ('author', models.CharField(max_length=255, verbose_name='Автор')),
                ('for_whom', models.CharField(choices=[('М', 'Мугалимдер үчүн'), ('О', 'Окуучулар үчүн'), ('А', 'Ата-энелер үчүн')], default='О', max_length=2, verbose_name='Кимдер үчүн')),
            ],
            options={
                'verbose_name': 'Кулактандыруу',
                'verbose_name_plural': 'Кулактандыруулар',
                'db_table': 'notifications',
            },
        ),
        migrations.CreateModel(
            name='NewsFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Файл жөнүндө маалымат')),
                ('file', models.FileField(null=True, upload_to='files/%Y/%m', verbose_name='Файл жүктөө')),
                ('news_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.news', verbose_name='Жаңылыктар үчүн файл жүктөө')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлдар',
                'db_table': 'news_files',
            },
        ),
    ]
