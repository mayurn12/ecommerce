# Generated by Django 3.0.7 on 2020-07-15 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('phone', models.CharField(default='0', max_length=1000)),
                ('zip_code', models.CharField(max_length=150)),
                ('total', models.CharField(default=0, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.FloatField()),
                ('discount_price', models.FloatField(default='As per Real Price')),
                ('product_category', models.CharField(max_length=200)),
                ('description', models.TextField(default='ADD PRODUCT DESCRIPTION')),
                ('product_image', models.ImageField(default='', upload_to='products/images')),
                ('add_time', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='profilepic.jpg', upload_to='products/profile')),
                ('about_you', models.CharField(default='Tell us about You', max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
