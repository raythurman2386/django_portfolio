# Generated by Django 4.1.4 on 2023-02-07 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Summary',
                'verbose_name_plural': 'Summary',
            },
        ),
    ]
