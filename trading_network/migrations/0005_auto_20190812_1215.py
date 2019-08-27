# Generated by Django 2.2.4 on 2019-08-12 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trading_network', '0004_auto_20190812_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.BigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='product_list',
            field=models.ManyToManyField(blank=True, related_name='ProductList', to='trading_network.Product'),
        ),
        migrations.DeleteModel(
            name='ProductList',
        ),
        migrations.AddField(
            model_name='price',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading_network.Company'),
        ),
        migrations.AddField(
            model_name='price',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading_network.Product'),
        ),
    ]
