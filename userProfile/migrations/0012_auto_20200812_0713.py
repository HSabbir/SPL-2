# Generated by Django 3.0.8 on 2020-08-12 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0011_auto_20200812_0635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='profile_of',
        ),
    ]
