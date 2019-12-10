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

def index(request):
    """
    blog的首页
    @param request
    @return 'blog/index.html'
    """ 
    article_list = Article.objects.all().order_by('-created_date')[0:5]
    for article in article_list:
        article.picture = 'blog/image/article_picture/{}'.format(article.picture)    

    context = {
        'article_list': article_list
    }
    
    return render(request, 'blog/index.html', context)

def detail(request,id):
    """
    blog的detail页
    @param request
    @return 'blog/detail.html'
    """ 
    try:
        article = Article.objects.get(id = id)
        if article != None:
            # 阅读量+1
            article.viewed()
            return render(request, 'blog/detail.html', {"article": article})
    except:
        return redirect(reverse('blog:index'))

def category(request,category_id):
    """
    blog的articles页（安装Category分类后的博文列表）
    @param request
    @return 'blog/articles.html'
    """ 
    article_list = Article.objects.filter(category_id=category_id)
    for article in article_list:
        article.picture = 'blog/image/article_picture/{}'.format(article.picture)     
    return render(request, 'blog/articles.html', {"article_list": article_list})

def tag(request,tag_name):
    """
    blog的articles页（安装Category分类后的博文列表）
    @param request
    @return 'blog/articles.html'
    """ 
    article_list = Article.objects.filter(tag__name = tag_name) #__:表示查询tag字段的name中是否包含了tag_name的字符串
    for article in article_list:
        article.picture = 'blog/image/article_picture/{}'.format(article.picture)     
    return render(request, 'blog/articles.html', {"article_list": article_list})

def about(request):
    """
    blog的about页
    @param request
    @return 'blog/about.html'
    """
    output = '这是blog的about页面'
    return HttpResponse(output)

@login_required
def archive(request):
    """
    blog的archive页
    @param request
    @return 'blog/archive.html'
    """    
    output = '这是blog的archive页面'
    return HttpResponse(output)


# 使用通用视图，比起传统的函数方式，django对通用视图有很多后台处理
# 只需要简单变量设置
class ArticleListView(ListView):
    model = Article
    template_name = 'blog/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'article_list'    #模板中使用的上下文变量名
    ordering = ['-last_mod_date']


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