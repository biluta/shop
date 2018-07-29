# Generated by Django 2.0.7 on 2018-07-26 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_auto_20180720_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_phone', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete='CASCADE', to='shop_app.Product')),
            ],
        ),
    ]