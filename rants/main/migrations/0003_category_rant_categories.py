# Generated by Django 4.1.7 on 2023-04-02 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_rants_rant_alter_rant_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='rant',
            name='categories',
            field=models.ManyToManyField(related_name='rants_categories', to='main.category'),
        ),
    ]
