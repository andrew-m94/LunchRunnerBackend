# Generated by Django 3.2.8 on 2022-01-19 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lunchgroups', '0004_lunchgroup_status'),
        ('orders', '0004_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='lunchgroup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lunchgroups.lunchgroup'),
        ),
    ]
