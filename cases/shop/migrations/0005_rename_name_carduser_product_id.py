# Generated by Django 4.2 on 2023-04-12 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_carduser_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carduser',
            old_name='name',
            new_name='product_id',
        ),
    ]
