# Generated by Django 4.1.5 on 2023-03-09 06:43

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_institute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='email',
            field=models.EmailField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='institute',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='institute_logo', validators=[django.core.validators.FileExtensionValidator(['svg', 'jpg', 'jpeg', 'png', 'avif', 'webp', 'pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'rar', '7zip'])], verbose_name='Institute Logo'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='mobile_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Mobile Number'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Institute Name'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='website',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]