# Generated by Django 4.0 on 2022-07-02 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='users/%Y%m%d/'),
        ),
    ]
