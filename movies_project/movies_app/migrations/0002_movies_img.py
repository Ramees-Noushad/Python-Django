# Generated by Django 4.2.2 on 2023-07-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default='sdkjskj', upload_to='gallery'),
            preserve_default=False,
        ),
    ]