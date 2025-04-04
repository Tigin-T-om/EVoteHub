# Generated by Django 4.2.20 on 2025-03-25 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_votingsession_candidate_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='votingsession',
            name='status',
            field=models.CharField(choices=[('scheduled', 'Scheduled'), ('active', 'Active'), ('completed', 'Completed'), ('published', 'Published'), ('cancelled', 'Cancelled')], default='scheduled', max_length=20),
        ),
    ]
