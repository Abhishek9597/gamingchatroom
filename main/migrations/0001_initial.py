# Generated by Django 4.1.7 on 2023-03-06 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('time_sent', models.DateTimeField(auto_now_add=True)),
                ('sender', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
