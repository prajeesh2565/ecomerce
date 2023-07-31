from django.urls import path
from . import views

app_name='shop'
urlpatterns = [

    path('',views.allcatproduct,name='allcatproduct'),
    path('<slug:c_slug>/',views.allcatproduct,name='products_by_cat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.products, name='product_details')

    ]


