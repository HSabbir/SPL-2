# Generated by Django 3.0.8 on 2020-07-14 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='HigherStudiesUniversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='HigherStudies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userProfile.Country')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userProfile.Profile')),
                ('study_domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userProfile.Domain')),
                ('university_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userProfile.HigherStudiesUniversity')),
            ],
        ),
    ]
