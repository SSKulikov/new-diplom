# Generated by Django 5.0.2 on 2024-03-28 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0016_delete_costumuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]