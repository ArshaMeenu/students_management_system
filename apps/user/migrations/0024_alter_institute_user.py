# Generated by Django 4.1.5 on 2023-03-09 07:46

import apps.user.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_institute_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='user',
            field=models.ForeignKey(blank=True, default=apps.user.models.get_user_type, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]