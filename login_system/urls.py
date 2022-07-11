from django.urls import path
from . import views


urlpatterns = [
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("new_booking", views.new_booking, name="new_booking"),
    path("all_booking", views.all_booking, name="all_booking"),
    path("bookings/<int:id>/change/", views.update_booking, name="update_booking"),
    path("", views.home, name="home")
]
