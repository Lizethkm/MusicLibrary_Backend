# Generated by Django 4.0.4 on 2022-04-25 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('artist', models.CharField(max_length=250)),
                ('album', models.CharField(max_length=250)),
                ('release_date', models.DateField(max_length=250)),
                ('genre', models.CharField(max_length=250)),
            ],
        ),
    ]
