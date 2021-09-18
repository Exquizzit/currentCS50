from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_item", views.newItem, name="new_item"),
    path("items/<str:itemName>", views.viewItem, name="viewItem")
]
