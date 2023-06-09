# Generated by Django 4.2.1 on 2023-06-02 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.IntegerField(primary_key=True, serialize=False)),
                ('branch_name', models.CharField(max_length=100)),
                ('branch_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Salesperson',
            fields=[
                ('salesperson_id', models.IntegerField(primary_key=True, serialize=False)),
                ('salesperson_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('sale_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sale_date', models.DateField()),
                ('sale_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Profit',
            fields=[
                ('profit_id', models.IntegerField(primary_key=True, serialize=False)),
                ('profit_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='APP.sale')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProgress',
            fields=[
                ('progress_id', models.IntegerField(primary_key=True, serialize=False)),
                ('progress_status', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.customer')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.sale')),
                ('salesperson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.salesperson')),
            ],
        ),
    ]
