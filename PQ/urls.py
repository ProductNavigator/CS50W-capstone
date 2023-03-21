
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("generate", views.generate, name="generate"),
    path("<int:set_id>", views.set, name="set"),
    path("user", views.user, name="user"),
    path("halloffame", views.halloffame, name="halloffame"),

]