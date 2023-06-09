# Generated by Django 4.1.6 on 2023-03-17 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0006_remove_profile_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='useraccount.profile'),
        ),
        migrations.AlterField(
            model_name='job',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='useraccount.profile'),
        ),
    ]
