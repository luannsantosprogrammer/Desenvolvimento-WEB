from django.urls import path
from . import views


urlpatterns = [
 path("",views.login_user,name="login"),
 path("create_user/",views.create_user,name="create_user"),
 path("logout_user/",views.logout_user,name="logout_user"),
 path("delete_item/<int:id>/",views.delete_item,name="delete_item"),
 path("buy/",views.buy,name="buy"),
]
