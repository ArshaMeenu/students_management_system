# Generated by Django 4.1.5 on 2023-03-20 08:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0045_alter_subjectallocation_lecturer'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(blank=True, null=True, upload_to='subject_files', validators=[django.core.validators.FileExtensionValidator(['svg', 'jpg', 'jpeg', 'png', 'avif', 'webp', 'pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'rar', '7zip'])], verbose_name='Subject Files')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.subject')),
            ],
        ),
    ]
