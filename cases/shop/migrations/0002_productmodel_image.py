# Generated by Django 4.2 on 2023-04-12 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to='images/'),
        ),
    ]
