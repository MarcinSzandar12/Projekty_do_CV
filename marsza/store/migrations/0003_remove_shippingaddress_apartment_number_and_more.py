# Generated by Django 4.1.1 on 2022-10-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='apartment_number',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='house_number',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='street_name',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
