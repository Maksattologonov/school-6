# Generated by Django 4.0.2 on 2022-03-04 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainAboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Мектеп жөнүндө маалыматтын темасы')),
                ('description', models.TextField(verbose_name='Мектеп жөнүндө маалымат')),
            ],
            options={
                'verbose_name': 'Башкы баракча маалыматы',
                'verbose_name_plural': 'Башкы баракча маалыматтары',
                'db_table': 'about_us',
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Аты-жөнү')),
                ('position', models.CharField(max_length=50, verbose_name='Позициясы')),
                ('lesson', models.CharField(max_length=50, verbose_name='Сабак')),
                ('timetable', models.TextField(verbose_name='График')),
                ('progress', models.TextField(verbose_name='Жетишкендиктери')),
                ('contacts', models.CharField(max_length=255, verbose_name='Байланышуу')),
                ('avatar', models.ImageField(upload_to='avatars')),
            ],
            options={
                'verbose_name': 'Мугалим',
                'verbose_name_plural': 'Мугалимдер',
                'db_table': 'teachers',
            },
        ),
        migrations.CreateModel(
            name='AboutUsFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Файл жөнүндө маалымат')),
                ('file', models.FileField(null=True, upload_to='files/%Y/%m', verbose_name='Файл жүктөө')),
                ('about_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_us_files', to='aboutUs.mainaboutus')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлдар',
                'db_table': 'files',
            },
        ),
    ]