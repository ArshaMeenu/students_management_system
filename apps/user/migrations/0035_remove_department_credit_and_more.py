# Generated by Django 4.1.5 on 2023-03-13 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0034_alter_course_course_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='credit',
        ),
        migrations.RemoveField(
            model_name='department',
            name='is_elective',
        ),
        migrations.RemoveField(
            model_name='department',
            name='level',
        ),
        migrations.RemoveField(
            model_name='department',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='department',
            name='year',
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='faculty',
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('Bachelor', 'Bachelor Degree'), ('Master', 'Master Degree')], max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='subjects',
            name='credit',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='subjects',
            name='is_elective',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='subjects',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.semester'),
        ),
        migrations.AddField(
            model_name='subjects',
            name='year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.academics'),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_id',
            field=models.CharField(blank=True, max_length=200, unique=True, verbose_name='department_id'),
        ),
    ]
