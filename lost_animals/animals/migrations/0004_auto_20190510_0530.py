# Generated by Django 2.1.4 on 2019-05-10 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_auto_20190510_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='uploaded_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]