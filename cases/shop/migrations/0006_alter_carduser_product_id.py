# Generated by Django 4.2 on 2023-04-13 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_name_carduser_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carduser',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productmodel'),
        ),
    ]
