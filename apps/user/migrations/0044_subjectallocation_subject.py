# Generated by Django 4.1.5 on 2023-03-17 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0043_remove_subjectallocation_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectallocation',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='allocated_subjects', to='user.subject'),
            preserve_default=False,
        ),
    ]
