# Generated by Django 4.1.7 on 2023-04-05 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_category_rant_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rant',
            old_name='rant',
            new_name='title',
        ),
    ]