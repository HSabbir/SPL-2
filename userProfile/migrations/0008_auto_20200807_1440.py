# Generated by Django 3.0.8 on 2020-08-07 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0007_auto_20200807_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='batch',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='college',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='session',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
