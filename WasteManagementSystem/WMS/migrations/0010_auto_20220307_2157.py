# Generated by Django 3.1 on 2022-03-07 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WMS', '0009_delete_addvehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='manager_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WMS.manager'),
        ),
    ]
