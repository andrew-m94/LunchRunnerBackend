# Generated by Django 3.2.8 on 2022-01-19 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lunchgroups', '0004_lunchgroup_status'),
        ('orders', '0005_alter_order_lunchgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='lunchgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lunchgroups.lunchgroup'),
        ),
    ]
