# Generated by Django 5.1 on 2024-09-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_remove_employer_profile_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='employer_pictures/'),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='jobseeker_pictures/'),
        ),
    ]
