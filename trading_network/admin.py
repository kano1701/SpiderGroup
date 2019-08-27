from django.contrib import admin

from .models import District, Category, TradingNetwork, Product, Company, Price


admin.site.register(District)
admin.site.register(Category)
admin.site.register(TradingNetwork)
admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Price)
