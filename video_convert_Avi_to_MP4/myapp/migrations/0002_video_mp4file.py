# Generated by Django 2.2.3 on 2019-07-18 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='mp4file',
            field=models.FileField(null=True, upload_to='mp4videos/', verbose_name=''),
        ),
    ]
