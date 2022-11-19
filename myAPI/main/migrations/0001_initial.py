# Generated by Django 3.2.5 on 2022-11-19 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('cr_t', models.DateTimeField(auto_now_add=True)),
                ('time', models.TimeField()),
                ('mode', models.JSONField(default=main.models.default_mode)),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('desc', models.CharField(blank=True, max_length=255)),
                ('main_c', models.CharField(blank=True, max_length=255)),
                ('fabr', models.CharField(blank=True, max_length=255)),
                ('presc_date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('pubk', models.TextField(blank=True, unique=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DrugsOnAlarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quant', models.PositiveIntegerField()),
                ('alarm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.alarm')),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.drug')),
            ],
        ),
        migrations.AddField(
            model_name='alarm',
            name='mach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.machine'),
        ),
        migrations.AddField(
            model_name='alarm',
            name='meds',
            field=models.ManyToManyField(blank=True, through='main.DrugsOnAlarm', to='main.Drug'),
        ),
    ]
