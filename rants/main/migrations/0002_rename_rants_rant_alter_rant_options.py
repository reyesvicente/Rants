# Generated by Django 4.1.7 on 2023-04-02 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rants',
            new_name='Rant',
        ),
        migrations.AlterModelOptions(
            name='rant',
            options={'verbose_name': 'rant', 'verbose_name_plural': 'rants'},
        ),
    ]
