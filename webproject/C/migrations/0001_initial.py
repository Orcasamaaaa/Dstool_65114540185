# Generated by Django 4.2.19 on 2025-03-05 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('Course_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Course_name', models.CharField(max_length=255)),
                ('Teacher_name', models.CharField(max_length=255)),
            ],
        ),
    ]
