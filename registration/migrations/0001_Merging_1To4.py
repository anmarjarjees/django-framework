# Generated by Django 3.1.5 on 2021-01-27 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('registration', '0001_initial'), ('registration', '0002_auto_20210113_1105'), ('registration', '0003_auto_20210113_1229'), ('registration', '0004_auto_20210118_1012')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnyClassName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshop_name', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=40)),
                ('last', models.CharField(max_length=40)),
                ('program_category', models.CharField(blank=True, max_length=35)),
                ('course', models.CharField(max_length=40)),
                ('course_description', models.TextField(blank=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('graduation_date', models.DateField()),
                ('average', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('last_modified_date', models.DateField(auto_now=True)),
                ('workshops', models.ManyToManyField(blank=True, to='registration.Workshop')),
            ],
        ),
    ]