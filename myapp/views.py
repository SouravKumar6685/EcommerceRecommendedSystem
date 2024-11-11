# myapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.db.models import Q
from .models import *

def product_list(request): 
    products = Product.objects.all()

    if query:= request.GET.get('q'):
          
        search_query = SearchQuery(query)

        products = products.annotate(
            query = SearchVector('title', 'description', 'category', 'tags__name', config='english')
        ).filter(query=query)


    context = {
        'products': products,
        'query': query,
    }

    return render(request, 'product_list.html', context)

def product_detail(request, product_id):  
    product = get_object_or_404(Product, id=product_id)
    product_tags = product.tags.all()
    similar_products = Product.objects.filter(
        Q(category=product.category) | Q(tags__in=product_tags)
    ).exclude(id=product_id).distinct().order_by('-rating')[:10]

    context = {
        'product': product,
        'similar_products': similar_products,
        'tags': product_tags,
    }

    return render(request, 'product_detail.html', context)
