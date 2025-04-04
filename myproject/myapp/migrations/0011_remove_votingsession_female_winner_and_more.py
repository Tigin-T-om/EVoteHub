# Generated by Django 4.2.20 on 2025-04-01 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_votingsession_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votingsession',
            name='female_winner',
        ),
        migrations.RemoveField(
            model_name='votingsession',
            name='male_winner',
        ),
        migrations.RemoveField(
            model_name='votingsession',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='votingsession',
            name='results_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='votingsession',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.officer'),
        ),
        migrations.AlterField(
            model_name='votingsession',
            name='status',
            field=models.CharField(choices=[('scheduled', 'Scheduled'), ('active', 'Active'), ('completed', 'Completed'), ('published', 'Published'), ('cancelled', 'Cancelled')], default='scheduled', max_length=20),
        ),
    ]
