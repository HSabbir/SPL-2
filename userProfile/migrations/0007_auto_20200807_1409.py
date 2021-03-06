# Generated by Django 3.0.8 on 2020-08-07 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0006_profile_additional_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_mail', models.CharField(blank=True, max_length=40, null=True)),
                ('facebook', models.CharField(blank=True, max_length=250, null=True)),
                ('github', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('linkedIn', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='higherstudies',
            name='country',
        ),
        migrations.RemoveField(
            model_name='higherstudies',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='higherstudies',
            name='study_domain',
        ),
        migrations.RemoveField(
            model_name='higherstudies',
            name='university_name',
        ),
        migrations.RemoveField(
            model_name='professionalinfo',
            name='organization_name',
        ),
        migrations.RemoveField(
            model_name='professionalinfo',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='project',
            name='domain',
        ),
        migrations.RemoveField(
            model_name='project',
            name='environment',
        ),
        migrations.RemoveField(
            model_name='project',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tools_and_technology',
        ),
        migrations.RemoveField(
            model_name='research',
            name='domain',
        ),
        migrations.RemoveField(
            model_name='research',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='additional_mail',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='github',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='linkedIn',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Domain',
        ),
        migrations.DeleteModel(
            name='Environment',
        ),
        migrations.DeleteModel(
            name='HigherStudies',
        ),
        migrations.DeleteModel(
            name='HigherStudiesUniversity',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
        migrations.DeleteModel(
            name='ProfessionalInfo',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Research',
        ),
        migrations.DeleteModel(
            name='ToolsAndTechnology',
        ),
        migrations.AddField(
            model_name='contact',
            name='Profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userProfile.Profile'),
        ),
    ]
