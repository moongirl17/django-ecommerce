# Generated by Django 4.2.1 on 2023-06-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_remove_order_customer_remove_orderitem_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='kategori',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Outwear')], max_length=2, null=True),
        ),
    ]