# Generated by Django 3.0.3 on 2020-02-20 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_n_registration_app', '0005_auto_20200215_0133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='liked_urls',
        ),
        migrations.RemoveField(
            model_name='user',
            name='wall_urls',
        ),
    ]
