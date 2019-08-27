from django.db import models


class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TradingNetwork(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return '%d: %s' % (self.id, self.name)


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    trading_network = models.ForeignKey(TradingNetwork, on_delete=models.CASCADE)
    product_list = models.ManyToManyField('Product', blank=True, related_name='ProductList')
    district_list = models.ManyToManyField('District', blank=True, related_name='DistrictList')


class Price(models.Model):
    price = models.BigIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
