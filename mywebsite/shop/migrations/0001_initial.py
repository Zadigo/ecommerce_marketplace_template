# Generated by Django 3.0.4 on 2020-08-06 10:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import shop.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AutomaticCollectionCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(default='NAW202086c4a94afc98', max_length=50)),
                ('condition', models.CharField(choices=[('is equal to', 'Is Equal To'), ('is not equal to', 'Is Not Equal To'), ('is greater than', 'Is Great Than'), ('is less than', 'Is Less Than'), ('starts with', 'Starts With'), ('ends with', 'Ends With'), ('contains', 'Contains'), ('does not contain', 'Does Not Contain'), ('yes', 'Yes'), ('no', 'No')], default='is equal to', max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('modified_on', models.DateField(auto_now=True)),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=80)),
                ('price_ht', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price_ttc', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(blank=True, max_length=5, null=True, validators=[shop.validators.generic_size_validator])),
                ('quantity', models.IntegerField(default=1, validators=[shop.validators.quantity_validator])),
                ('anonymous', models.BooleanField(default=False)),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on', '-pk'],
            },
        ),
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=50)),
                ('transaction', models.CharField(default='4bad-911cac229bca39e61862e83a0298049433b81a205c92771b37fbfcddf24d0a07', max_length=200)),
                ('payment', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('accepted', models.BooleanField(default=False)),
                ('shipped', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('refund', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('tracking_number', models.CharField(blank=True, max_length=50, null=True)),
                ('delivery', models.CharField(choices=[('standard', 'Standard')], default='standard', max_length=50)),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on', '-pk'],
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='NAW5946Q', max_length=10)),
                ('value', models.IntegerField(default=5)),
                ('value_type', models.CharField(choices=[('percentage', 'Percentage'), ('fixed amount', 'Fixed Amount'), ('free shipping', 'Free Shipping')], default='percentage', max_length=50)),
                ('on_entire_order', models.BooleanField(default=False, help_text='Apply on an entire order')),
                ('minimum_purchase', models.IntegerField(default=0)),
                ('minimum_quantity', models.IntegerField(default=0)),
                ('usage_limit', models.IntegerField(default=0, help_text='Number of times a code can be used in total')),
                ('active', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('variant', models.CharField(default='Noir', max_length=30)),
                ('aws_key', models.CharField(blank=True, max_length=50, null=True, verbose_name='AWS folder key')),
                ('aws_slug_name', models.CharField(blank=True, help_text='File name on AWS', max_length=100, null=True)),
                ('aws_image', models.BooleanField(default=False)),
                ('main_image', models.BooleanField(default=False, help_text='Indicates if this is the main image for the product')),
                ('url', models.URLField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='LookBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('create_on', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('reference', models.CharField(default='OZ47856A08F979', max_length=30)),
                ('gender', models.CharField(choices=[('femme', 'Femme'), ('homme', 'Homme')], default='femme', max_length=50)),
                ('description', models.TextField(blank=True, max_length=280, null=True)),
                ('description_html', models.TextField(blank=True, max_length=800, null=True)),
                ('description_objects', models.TextField(blank=True, max_length=800, null=True)),
                ('price_ht', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discount_pct', models.IntegerField(blank=True, default=10)),
                ('discounted_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('price_valid_until', models.DateField(default=datetime.date(2020, 9, 5))),
                ('quantity', models.IntegerField(blank=True, default=0)),
                ('sku', models.CharField(blank=True, help_text='ex. BCLOGO-GRIS-SMA', max_length=50, null=True)),
                ('google_category', models.CharField(choices=[('5424', 'Skirts'), ('212', 'Tops'), ('207', 'Shorts'), ('2271', 'Dresses'), ('214', 'Bras'), ('178', 'Accessories'), ('7366', 'Flyingtoyaccessories')], default='212', max_length=5)),
                ('in_stock', models.BooleanField(default=True)),
                ('discounted', models.BooleanField(default=False)),
                ('our_favorite', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('private', models.BooleanField(default=False, help_text='Product is on accessible by sharing the direct link')),
                ('slug', models.SlugField()),
                ('to_be_published_on', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('last_modified', models.DateField(auto_now=True)),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on', '-pk'],
            },
        ),
        migrations.CreateModel(
            name='ProductCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('femme', 'Femme'), ('homme', 'Homme')], default='femme', max_length=50)),
                ('view_name', models.CharField(max_length=50)),
                ('image', models.URLField(blank=True, null=True)),
                ('presentation_text', models.TextField(blank=True, max_length=300, null=True)),
                ('google_description', models.CharField(blank=True, max_length=160, null=True)),
                ('show_presentation', models.BooleanField(default=False)),
                ('automatic', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=1)),
                ('text', models.TextField(max_length=300)),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(blank=True, max_length=100, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=3, null=True, validators=[shop.validators.generic_size_validator])),
                ('verbose_name', models.CharField(blank=True, max_length=50, null=True)),
                ('in_stock', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddIndex(
            model_name='variant',
            index=models.Index(fields=['name'], name='shop_varian_name_256798_idx'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='customer_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.CustomerOrder'),
        ),
        migrations.AddField(
            model_name='review',
            name='customer_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.CustomerOrder'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productcollection',
            name='criterion',
            field=models.ManyToManyField(blank=True, to='shop.AutomaticCollectionCriteria'),
        ),
        migrations.AddField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.ProductCollection'),
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(to='shop.Image'),
        ),
        migrations.AddField(
            model_name='product',
            name='variant',
            field=models.ManyToManyField(blank=True, to='shop.Variant'),
        ),
        migrations.AddField(
            model_name='lookbook',
            name='products',
            field=models.ManyToManyField(to='shop.Product'),
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['url'], name='shop_image_url_972fe2_idx'),
        ),
        migrations.AddField(
            model_name='discount',
            name='collection',
            field=models.ForeignKey(blank=True, help_text='Apply on an entire collection', null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.ProductCollection'),
        ),
        migrations.AddField(
            model_name='discount',
            name='product',
            field=models.ForeignKey(blank=True, help_text='Apply on a specific product', null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Product'),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='cart',
            field=models.ManyToManyField(blank=True, to='shop.Cart'),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Discount'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['reference', 'collection', 'name'], name='shop_produc_referen_cd33b7_idx'),
        ),
        migrations.AddIndex(
            model_name='customerorder',
            index=models.Index(fields=['payment'], name='shop_custom_payment_49b892_idx'),
        ),
        migrations.AddIndex(
            model_name='cart',
            index=models.Index(fields=['price_ht', 'quantity'], name='shop_cart_price_h_37ab93_idx'),
        ),
    ]
