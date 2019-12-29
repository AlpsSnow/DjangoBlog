from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required #只有已经登录的用户才能访问视图
from .models import Tag, Category, Article

# 使用通用视图
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# 个别通用视图类访问前必须先登录，如果没有登录，重定向到登录页面
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib import messages

# Create your views here.
def about(request):
    """
    blog的about页
    @param request
    @return 'blog/about.html'
    """
    output = '这是blog的about页面'
    return HttpResponse(output)

# 使用通用视图，比起传统的函数方式，django对通用视图有很多后台处理
# 只需要简单变量设置
class ArticleListView(ListView):
    model = Article
    template_name = 'blog/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'article_list'    #模板中使用的上下文变量名
    ordering = ['-last_mod_date']
    paginate_by = 5 #分页，设置每页显示的博文个数


class ArticleDetailView(DetailView):
    model = Article   
    template_name = 'blog/detail.html'

    # 覆写 get_object 方法的目的是因为需要对 Article 的 点击量的值进行更新
    def get_object(self, queryset=None):        
        article = super(ArticleDetailView, self).get_object(queryset=None)
        article.viewed()
        return article    

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'digest', 'content', 'category','tag']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request,f'成功创建博文!')
        return super().form_valid(form)   

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'digest', 'content', 'category','tag']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request,f'成功更新博文!')
        return super().form_valid(form)

    # 检查请求更新博文的用户是否是作者
    def test_func(self):
        Article = self.get_object()
        if self.request.user == Article.author:
            return True
        return False

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = '/'

    # 检查请求删除博文的用户是否是作者
    def test_func(self):
        Article = self.get_object()        
        if self.request.user == Article.author:            
            return True
        return False

class UserArticleListView(ListView):
    model = Article
    template_name = 'blog/articles.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'article_list'    #模板中使用的上下文变量名
    paginate_by = 5 #分页，设置每页显示的博文个数

    def get_queryset(self):
        article_list= Article.objects.filter(author__username = self.kwargs['username']).order_by('-last_mod_date') #从self.kwargs中（即，从url参数中）获取用户名
        return article_list

class CategoryListView(ListView):
    model = Article
    template_name = 'blog/articles.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'article_list'    #模板中使用的上下文变量名
    paginate_by = 5 #分页，设置每页显示的博文个数

    def get_queryset(self):
        article_list= Article.objects.filter(category_id = self.kwargs['category_id']).order_by('-last_mod_date')    
        return article_list

class TagListView(ListView):
    model = Article
    template_name = 'blog/articles.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'article_list'    #模板中使用的上下文变量名
    paginate_by = 5 #分页，设置每页显示的博文个数
    def get_queryset(self):
        article_list= Article.objects.filter(tag__name = self.kwargs['tag_name']).order_by('-last_mod_date')
        return article_list