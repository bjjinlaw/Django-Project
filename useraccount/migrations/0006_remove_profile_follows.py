# Generated by Django 4.1.6 on 2023-03-16 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0005_profile_follows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follows',
        ),
    ]
