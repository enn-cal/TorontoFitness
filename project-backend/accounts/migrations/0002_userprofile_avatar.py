# Generated by Django 4.1.2 on 2022-11-02 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='avatars'),
        ),
    ]
