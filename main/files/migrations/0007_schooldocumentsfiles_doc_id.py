# Generated by Django 4.0.2 on 2022-03-15 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0006_schooldocuments_schooldocumentsfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='schooldocumentsfiles',
            name='doc_id',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='files.schooldocuments', verbose_name='Файл'),
            preserve_default=False,
        ),
    ]
