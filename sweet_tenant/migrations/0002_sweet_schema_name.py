# Generated by Django 4.2 on 2023-04-14 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_tenant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sweet',
            name='schema_name',
            field=models.CharField(default='public', max_length=100),
        ),
    ]
