# Generated by Django 3.1 on 2022-03-07 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WMS', '0010_auto_20220307_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='manager_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WMS.manager'),
        ),
    ]
