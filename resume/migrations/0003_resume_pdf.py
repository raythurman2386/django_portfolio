# Generated by Django 4.1.4 on 2023-02-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_contact_education_employment_projects_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume_PDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('pdf_file', models.FileField(upload_to='media')),
            ],
        ),
    ]
