# Generated by Django 4.1.5 on 2023-03-10 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_alter_institute_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='session',
        ),
        migrations.AddField(
            model_name='semester',
            name='is_current_semester',
            field=models.BooleanField(default=False),
        ),
    ]