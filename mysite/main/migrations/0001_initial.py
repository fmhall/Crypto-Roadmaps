# Generated by Django 2.1.7 on 2019-03-21 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('project_description', models.TextField()),
                ('project_published', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
