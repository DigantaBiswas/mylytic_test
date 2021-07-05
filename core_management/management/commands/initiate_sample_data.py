from django.core.management.base import BaseCommand

from core_management.models import Category, Product


class Command(BaseCommand):
    help = 'Creates objects for Category, Product model '

    def handle(self, *args, **kwargs):
        new_category = Category()
        new_category.name = 'Fruits'
        new_category.save()

        new_product = Product()
        new_product.product_code = "5532"
        new_product.name = "Apple"

        new_product.stock_in_units = 50
        new_product.unit_price = 30
        new_product.save()
        new_product.category.add(new_category)

        new_product = Product()
        new_product.product_code = "5871"
        new_product.name = "Grape"

        new_product.stock_in_units = 30
        new_product.unit_price = 10
        new_product.save()
        new_product.category.add(new_category)

        print("Category and product created for testing")


