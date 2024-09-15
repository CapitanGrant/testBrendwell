from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Product


def index(request):
    prod = Product.objects.all()
    return render(request, 'index.html', {'prod': prod})


@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        try:
            price = float(price)
            if price <= 0:
                return JsonResponse({'error': 'Цена должна быть положительным числом.'}, status=400)
            product = Product.objects.create(name=name, description=description, price=price)
            return JsonResponse({'message': 'Продукт добавлен', 'id': product.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'index.html')


def get_products(request):
    products = Product.objects.all()
    products_list = []
    for product in products:
        products_list.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price
        })
    return JsonResponse(products_list, safe=False)
