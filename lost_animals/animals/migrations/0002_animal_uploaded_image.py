# Generated by Django 2.1.4 on 2019-05-10 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='uploaded_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
