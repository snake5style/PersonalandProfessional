# Generated by Django 3.0.4 on 2020-05-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('future_projects', '0009_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='future_projects/img'),
        ),
    ]
