# Generated by Django 3.0.1 on 2019-12-29 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20191229_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='total_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='сумма продажи'),
        ),
    ]
