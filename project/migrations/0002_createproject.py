# Generated by Django 3.0.8 on 2020-09-14 14:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workingSkills', '0002_auto_20200909_0628'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=100)),
                ('domain', models.ManyToManyField(to='workingSkills.Domain')),
                ('environment', models.ManyToManyField(to='workingSkills.Environment')),
                ('profile', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('tools_and_technology', models.ManyToManyField(to='workingSkills.ToolsAndTechnology')),
            ],
        ),
    ]