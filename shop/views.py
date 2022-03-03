from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Product
from django.utils import timezone
from .forms import ProductForm

def index(request):
    context = {}
    context["product_list"] = Product.objects.all()
       
    return render(request, "shop/index.html", context)


def single(request, id):
    context = {}
    context["data"] = Product.objects.get(id=id)
    context["quantity"] = range(1, context["data"].quantity+1)

    return render(request, "shop/single.html", context)

def create(request):
    context = {}
    form = ProductForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/shop")
    context["form"] = form
    
    return render(request, "shop/create.html", context)

def update(request, id):
    context ={}
    item = get_object_or_404(Product, id = id)
    form = ProductForm(request.POST or None, instance = item)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(f"/shop/{id}")

    context["form"] = form
    return render(request, "shop/update.html", context)

def buy(request, id):
    quantity = request.POST.get('quantity')

    item = get_object_or_404(Product, id=id)

    Product.objects.filter(id = id).update(quantity = item.quantity - int(quantity))
    item.refresh_from_db()

    return HttpResponseRedirect("/shop")