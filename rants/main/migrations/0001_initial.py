# Generated by Django 4.1.7 on 2023-03-31 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rant', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
            ],
        ),
    ]
