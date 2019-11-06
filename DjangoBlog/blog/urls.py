from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.index,name='index'),
    path('archive',views.archive,name='archive'),
    path('about',views.about,name='about'),
    path('detail/<int:id>',views.detail,name='detail')
]