# Generated by Django 4.2.1 on 2023-06-05 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0010_inventory_remove_sale_sale_amount_sale_sale_volume_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='inventory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='APP.inventory'),
        ),
    ]
