# Generated by Django 4.2.20 on 2025-03-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_student_gender_alter_votingsession_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='student_profiles/'),
        ),
    ]
