# Generated by Django 3.1.4 on 2022-01-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DumpArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('destination', models.CharField(max_length=50)),
                ('dimension', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Garbage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('garbage_type', models.CharField(max_length=50)),
                ('cost_per_unit', models.CharField(max_length=50)),
                ('garbage_quantity', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('emial', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_arrival', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('number', models.CharField(max_length=150)),
                ('size', models.CharField(max_length=20, null=True)),
                ('color', models.CharField(max_length=10)),
                ('brand', models.CharField(max_length=150)),
                ('model_no', models.CharField(max_length=50)),
            ],
        ),
    ]