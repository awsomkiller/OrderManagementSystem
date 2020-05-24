from django.shortcuts import render,redirect
from .models import product, Orders
from math import ceil


# Create your views here.
def home(request):
    return render(request, 'home.html')


def shop(request):
    if request.user.is_authenticated:
        products = product.objects.all()
        n = len(products)
        nslide = n//4 + ceil((n/4)-(n//4))
        params = {'no_of_slides': nslide, 'range': range(nslide), 'products': products}
        return render(request, 'shop.html', params)
    else:
        return redirect('login')


def checkout(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            thank = True
            item_json = request.POST.get('itemJson', '')
            current_user = request.user
            order = Orders(item_json=item_json, accountId=current_user)
            print(item_json)
            order.save()
            return render(request, 'checkout.html', {'thank': thank})
        else:
            return render(request, 'checkout.html')
    else:
        return redirect('login')
