# Generated by Django 4.2.1 on 2023-06-14 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0025_alter_public_massage_chair_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.product', unique=True),
        ),
    ]
