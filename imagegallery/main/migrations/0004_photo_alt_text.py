# Generated by Django 4.0.4 on 2022-05-23 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_photo_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='alt_text',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]