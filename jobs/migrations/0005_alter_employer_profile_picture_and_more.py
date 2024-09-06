# Generated by Django 5.1 on 2024-09-05 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_employer_profile_picture_jobseeker_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='profile_picture',
            field=models.ImageField(default='media/blank.png', upload_to='profile_pictures/'),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='profile_picture',
            field=models.ImageField(default='media/blank.png', upload_to='profile_pictures/'),
        ),
    ]
