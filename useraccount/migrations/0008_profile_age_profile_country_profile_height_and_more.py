# Generated by Django 4.1.6 on 2023-03-20 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0007_alter_education_profile_alter_job_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='marital_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mother_tongue',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='religion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
