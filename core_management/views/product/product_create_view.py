from django.views.generic.edit import CreateView

from core_management.models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['product_code', 'name', 'stock_in_units', 'unit_price', 'category', ]

    def get_template_names(self):
        return ['core_management/generic_create.html']
