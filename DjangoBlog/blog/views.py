from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from .models import Tag, Category, Article

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
    return render(request, 'blog/index.html', {"article_list": article_list})

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
        return redirect(reverse('blog:root'))

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

def archive(request):
    """
    blog的archive页
    @param request
    @return 'blog/archive.html'
    """    
    return redirect(reverse('blog:root')) #'blog/archive'的URL将重定向到blog:root的路由
