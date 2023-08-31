from django.shortcuts import render, redirect


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
        list_of_names = []
    list_of_prices = []
    for phone in phones:
        list_of_names.append(phone.name)
        list_of_prices.append(phone.price)
    context = {
        'phones': phones,
        'name': sorted(list_of_names),
        'max_price': sorted(list_of_prices, reverse=True),
        'min_price': sorted(list_of_prices),
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phones': phones,
        'slug': slug
    }
    return render(request, template, context)
