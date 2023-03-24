# Generated by Django 4.1.6 on 2023-03-03 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=255)),
                ('partner_name', models.CharField(max_length=255)),
                ('your_email', models.CharField(max_length=255)),
                ('partner_email', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='story')),
            ],
        ),
    ]