# Generated by Django 4.1.5 on 2023-03-13 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0036_subjects_teache'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='teache',
        ),
    ]