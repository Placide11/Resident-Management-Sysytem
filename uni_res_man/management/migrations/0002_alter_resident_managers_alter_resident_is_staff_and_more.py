# Generated by Django 5.1.1 on 2024-10-18 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='resident',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='resident',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='resident',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
