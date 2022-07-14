from django.urls import path
from . import views


urlpatterns = [
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("customers", views.customers, name="customers"),
    path("customers/create", views.new_customer, name="new_customer"),
    path("bookings/create", views.new_booking, name="new_booking"),
    path("bookings", views.bookings, name="bookings"),
    path("daily_bookings", views.all_booking, name="all_booking"),
    path("bookings/<int:id>/update/", views.update_booking, name="update_booking"),
    path("", views.home, name="home")
]
