# Generated by Django 3.2.6 on 2021-08-27 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210827_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=11),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=11),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='total_price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=11),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=11),
        ),
    ]
