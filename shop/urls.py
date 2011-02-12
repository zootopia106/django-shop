#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from shop.models.productmodel import Product, Category
from shop.views import ShopDetailView, ShopListView
from shop.views.cart import CartDetails
from shop.views.category import CategoryDetailView

# Loop through payment backends and mount the modules in pay/
urlpatterns = patterns('',
    (r'^pay/$', include('shop.payment.urls')),
    (r'^ship/$', include('shop.shipping.urls')),
    
    url(r'^cart/$', CartDetails.as_view()),
    
    # Products
    url(r'^product/(?P<slug>[0-9A-Za-z-_.//]+)/$',
        ShopDetailView.as_view(model=Product),
        name='product_detail'
        ),
    url(r'^products/$',
        ShopListView.as_view(model=Product),
        name='product_list'
        ),
        
    # Categories
    url(r'^categories/$',
        ShopListView.as_view(model=Category),
        name='category_list'
        ),
    url(r'^category/(?P<slug>[0-9A-Za-z-_.//]+)/$',
        CategoryDetailView.as_view(),
        name='category_detail'
        ),
)
