import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from core_management.models import Order, Product, Cart


class OrderCreateView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(OrderCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        product_list = Product.objects.all()
        context = {
            'products': product_list
        }
        return render(request, 'core_management/order_create.html', context)

    def post(self, request):
        data = json.loads(request.POST.get('data', None))
        if not data:
            return render(request, 'core_management/order_create.html')

        orders = data.get("orders")
        customer_name = data.get("name")
        customer_phone = data.get("phone")
        customer_email = data.get("email")
        products = Product.objects.all().values('id', 'stock_in_units', 'name')
        product_id_pk_dict = {}
        for item in products:
            product_id_pk_dict[str(item['id'])] = {'stock': str(item['stock_in_units']), 'product': item['name']}
        for key, value in orders.items():
            if int(product_id_pk_dict.get(key).get('stock'), 0) < int(value):
                response = JsonResponse({"success": False, "error": "Not enough stock for {}".format(
                    product_id_pk_dict.get(key).get('product'))})
                response.status_code = 403
                return response

        new_order = Order()
        new_order.customer_phone = customer_phone
        new_order.customer_email = customer_email
        new_order.customer_name = customer_name
        new_order.save()

        for key, value in orders.items():
            new_cart = Cart()
            new_cart.product_id = int(key)
            new_cart.quantity = int(value)
            new_cart.order = new_order
            new_cart.save()

        return redirect('core_management/order_list.html')
