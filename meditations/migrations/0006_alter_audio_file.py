# Generated by Django 3.2.9 on 2021-11-26 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditations', '0005_alter_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='file',
            field=models.FileField(upload_to='sounds'),
        ),
    ]
