# Generated by Django 2.2.1 on 2019-06-21 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilemodel',
            old_name='description',
            new_name='bio',
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='profile_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
