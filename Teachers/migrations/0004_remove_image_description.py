# Generated by Django 4.2 on 2023-04-12 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0003_image_delete_uploadimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='description',
        ),
    ]
