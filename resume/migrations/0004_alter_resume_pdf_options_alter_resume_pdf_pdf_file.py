# Generated by Django 4.1.4 on 2023-02-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_resume_pdf'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resume_pdf',
            options={'verbose_name': 'Resume', 'verbose_name_plural': 'Resume'},
        ),
        migrations.AlterField(
            model_name='resume_pdf',
            name='pdf_file',
            field=models.FileField(upload_to='media/'),
        ),
    ]
