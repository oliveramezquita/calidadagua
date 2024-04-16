# Generated by Django 4.2.10 on 2024-04-16 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=150, null=True)),
                ('type', models.CharField(max_length=50)),
                ('values', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('season', models.CharField(max_length=50)),
                ('activated', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=150, null=True)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=25, null=True)),
                ('institution', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('activated', models.BooleanField()),
            ],
        ),
    ]
