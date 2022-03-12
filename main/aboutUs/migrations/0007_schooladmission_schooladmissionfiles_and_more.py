# Generated by Django 4.0.2 on 2022-03-12 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutUs', '0006_alter_aboutusfiles_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolAdmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Аталышы')),
                ('description', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Мектепке кабыл алуу',
                'verbose_name_plural': 'Мектепке кабыл алуу маалыматтары',
                'db_table': 'school_admission',
            },
        ),
        migrations.CreateModel(
            name='SchoolAdmissionFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Аталышы')),
                ('file', models.FileField(upload_to='files/%Y/%m', verbose_name='Файл жүктөө')),
            ],
            options={
                'verbose_name': 'Мектепке кабыл алуу файлы',
                'verbose_name_plural': 'Мектепке кабыл алуу файлдары',
                'db_table': 'school_admission_files',
            },
        ),
        migrations.AlterField(
            model_name='gloryboard',
            name='glory_whom',
            field=models.CharField(choices=[('M', 'Мугалим'), ('O', 'Окуучу')], default='Окуучу', max_length=20, verbose_name='Сыйлануучу'),
        ),
    ]
