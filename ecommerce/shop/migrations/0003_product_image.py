# Generated by Django 5.1.1 on 2024-10-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_admin_cart_category_coupon_order_paymentmethod_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]
