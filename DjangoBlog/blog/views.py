from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    blog的首页
    @param request
    @return 'blog/index.html'
    """
    output = '这是blog的首页'
    return HttpResponse(output)

def detail(request,id):
    """
    blog的detail页
    @param request
    @return 'blog/detail.html'
    """
    output = '这是blog的详细页面，第 %s 篇博文' % id
    return HttpResponse(output)

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
