# Generated by Django 5.0.2 on 2024-03-15 01:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0008_alter_files_linkuiid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='linkUiid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
