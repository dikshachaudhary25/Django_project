from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu/<int:item_id>/', views.menu_detail, name="menu_detail"),
    path('menu-item/<int:pk>/', views.display_menu_items, name="display_menu_items"),
]
