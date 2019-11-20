from django.urls import path
from . import views

app_name = 'users'  #定义应用程序的命名空间(访问路由地时候可以用“应用命名空间：路由name”)

urlpatterns = [
    path('', views.register, name='register')
]