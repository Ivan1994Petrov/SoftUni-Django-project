# Generated by Django 2.1.4 on 2019-05-11 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0008_animal_found_or_lost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='found_or_lost',
            new_name='Статус на животното',
        ),
    ]