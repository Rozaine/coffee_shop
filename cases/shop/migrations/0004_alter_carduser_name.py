# Generated by Django 4.2 on 2023-04-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_carduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carduser',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]