# Generated by Django 4.1.5 on 2023-03-06 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_course_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='year',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=0),
        ),
    ]
