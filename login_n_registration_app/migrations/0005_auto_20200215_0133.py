# Generated by Django 3.0.3 on 2020-02-15 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_n_registration_app', '0004_auto_20200214_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='liked_urls',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='wall_urls',
            field=models.TextField(default=''),
        ),
    ]
