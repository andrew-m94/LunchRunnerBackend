# Generated by Django 3.2.8 on 2022-01-19 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_lunchgroup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='lunchgroup',
            new_name='lunchgroup_id',
        ),
    ]
