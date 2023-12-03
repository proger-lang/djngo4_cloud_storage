from django.shortcuts import render
from django.http import HttpResponse
from .models import Product



def index(request):
    items = Product.objects.all()
    context = {
        'items':items
    }
    return render(request, "shop1/index.html", context)


def index_id(request, m_id):
     item = Product.objects.get(id=m_id)
     context = {
        'items':item
    }
     return render(request, "shop1/detail.html",context=context)

