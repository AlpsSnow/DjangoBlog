from django.urls import path
from . import views

# 使用通用视图
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    UserArticleListView,
    CategoryListView,
    TagListView
)

app_name = 'blog'  #定义应用程序的命名空间(访问路由地时候可以用“应用命名空间：路由name”)

urlpatterns = [
    #path('', views.index, name='root'), 
    #path('index/', views.index, name='index'),
    #path('detail/<int:id>',views.detail,name='detail'),
    #path('articles/category/<int:category_id>',views.category,name='category'),
    #path('articles/tag/<str:tag_name>',views.tag, name='tag')
    path('', ArticleListView.as_view(), name='root'),   # 使用通用视图    
    path('index/', ArticleListView.as_view(), name='index'),    # 使用通用视图
    path('about/',views.about,name='about'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),   # 使用通用视图
    path('detail/new/', ArticleCreateView.as_view(), name='create'),   # 使用通用视图
    path('detail/<int:pk>/update/', ArticleUpdateView.as_view(), name='update'),   # 使用通用视图
    path('detail/<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete'),   # 使用通用视图
    path('articles/user/<str:username>',UserArticleListView.as_view(),name='userarticlelist'),  # 使用通用视图
    path('articles/category/<int:category_id>',CategoryListView.as_view(),name='category'),
    path('articles/tag/<str:tag_name>',TagListView.as_view(), name='tag')
]  