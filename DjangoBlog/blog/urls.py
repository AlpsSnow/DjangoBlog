from django.urls import path
from . import views

app_name = 'blog'  #定义应用程序的命名空间

urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='index'),
    path('archive/',views.archive,name='archive'),
    path('about/',views.about,name='about'),
    path('detail/<int:id>',views.detail,name='detail')
]