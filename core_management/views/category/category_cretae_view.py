from django.views.generic.edit import CreateView

from core_management.models import Product, Category


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']

    def get_template_names(self):
        return ['core_management/generic_create.html']
