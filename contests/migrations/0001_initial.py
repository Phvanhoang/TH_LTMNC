# Generated by Django 3.1.7 on 2021-04-26 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('contest_type', models.CharField(max_length=20)),
                ('start', models.DateTimeField(verbose_name='date-published')),
                ('length', models.DurationField()),
                ('status', models.CharField(max_length=20)),
                ('participant', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('solved', models.IntegerField()),
                ('time_limit', models.IntegerField()),
                ('memory_limit', models.IntegerField()),
                ('description', models.TextField()),
                ('input', models.TextField()),
                ('output', models.TextField()),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.contest')),
            ],
        ),
    ]
