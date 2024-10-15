from typing import Any
from django.db.models.query import QuerySet
from django.http import Http404
from django.views.generic import DetailView, ListView

from goods.utils import q_search
from .models import Products

from django.core.cache import cache
import pickle
import hashlib

class CatalogView(ListView):
    model = Products
    # queryset = Products.objects.all().order_by("-id")
    template_name = "goods/catalog.html"
    context_object_name = "goods"
    paginate_by = 3
    allow_empty = False
    # чтоб удобно передать в методы
    slug_url_kwarg = "category_slug"


    CACHE_TIMEOUT = 60 * 15

    def get_cache_key(self) -> str:

        category_slug = self.kwargs.get(self.slug_url_kwarg, 'all')
        on_sale = self.request.GET.get("on_sale", "false")
        order_by = self.request.GET.get("order_by", "default")
        query = self.request.GET.get("q", "")
        page = self.request.GET.get("page", "1")

        key_string = f"catalog:{category_slug}:{on_sale}:{order_by}:{query}:page{page}"
        
        return hashlib.md5(key_string.encode('utf-8')).hexdigest()

    def get_queryset(self):
        cache_key = self.get_cache_key()
        print(f"Caching with key: {cache_key}") 
        cached_data = cache.get(cache_key)

        category_slug = self.kwargs.get(self.slug_url_kwarg)
        on_sale = self.request.GET.get("on_sale")
        order_by = self.request.GET.get("order_by")
        query = self.request.GET.get("q")

        if category_slug == "all":
            goods = super().get_queryset()
        elif query:
            goods = q_search(query)
        else:
            goods = super().get_queryset().filter(category__slug=category_slug)
            if not goods.exists():
                raise Http404()

        if on_sale:
            goods = goods.filter(discount__gt=0)

        if order_by and order_by != "default":
            goods = goods.order_by(order_by)
        
        cache.set(cache_key, pickle.dumps(goods), self.CACHE_TIMEOUT)

        return goods
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Каталог"
        context["slug_url"] = self.kwargs.get(self.slug_url_kwarg)
        return context






# def catalog(request, category_slug=None):

#     page = request.GET.get('page',1)
#     on_sale = request.GET.get('on_sale',None)
#     order_by = request.GET.get('order_by',None)
#     query = request.GET.get('q',None)
    

#     if category_slug == 'all':
#         goods = Products.objects.all()
#     elif query:
#         goods = q_search(query)
#     else:
#         goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
        
#     if on_sale:
#         goods = goods.filter(discount__gt=0)
    
#     if order_by and order_by != "default":
#         goods = goods.order_by(order_by)

#     paginator = Paginator(goods, 3)
#     current_page = paginator.page(int(page))

#     context = {
#         'title': 'Home - Каталог',
#         'goods':current_page,
#         'slug_url':category_slug
#     }

#     return render(request,'goods/catalog.html',context)



class ProductView(DetailView):
    #model = Products
    template_name = 'goods/product.html'
    slug_url_kwarg = "product_slug"
    context_object_name = "product"
    #slug_field = "slug"
    def get_object(self, queryset=None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context



# def product(request,product_slug):
#     product = Products.objects.get(slug=product_slug)
#     context = {
#         'product':product
#     }


#     return render(request,'goods/product.html',context=context)