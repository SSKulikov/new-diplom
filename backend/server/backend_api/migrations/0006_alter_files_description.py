# Generated by Django 5.0.2 on 2024-03-10 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0005_alter_files_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
