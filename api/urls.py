from django.urls import path
from . import views

urlpatterns = [
    # path('', views.apiOverview, name='apiOverview'),
    path('product-list/', views.ShowAll, name='product-list'),
    path('product-create/', views.CreateProduct, name='product-create'),
    path('logout/', views.logout_view, name='logout'),
]