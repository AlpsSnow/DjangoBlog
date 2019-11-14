from django.shortcuts import render
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
    article = Article.objects.get(id = id)
    # 阅读量+1    
    article.viewed()
    return render(request, 'blog/detail.html', {"article": article})

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
    output = '这是blog的archive页面'
    return HttpResponse(output)
