from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category


def home(request):
    items=None
    category=Category.objects.all()
    catID = request.GET.get('cat')
    if catID:
        items=Product.objects.filter(category=catID)
    else:
        items=Product.objects.all()

    context={
        'items':items,
        'category':category,

    }

    return render(request,'store/home-page.html',context)


def order(request):
    return render(request,'store/order.html')


def register(request):
    return render(request,'store/register.html')


