from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path('admin/', admin.site.urls),
    path('rest/', include('rest.urls')),

    # path('', views.cart_summary, name="cart_summary"),
    # path('add/', views.cart_add, name="cart_add"),
    # path('delete/', views.cart_delete, name="cart_delete"),
    # path('update/', views.cart_summary, name="cart_summary"),

]
