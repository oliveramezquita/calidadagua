# Generated by Django 4.2.10 on 2024-04-16 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formsapp', '0002_rename_site_reference_id_site_site_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='photo_1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='site',
            name='photo_2',
            field=models.TextField(),
        ),
    ]
