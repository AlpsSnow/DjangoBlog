#from django.conf import settings
from .models import Tag, Category, Article, CarouselImg

"""
blog app上下文渲染器
"""

#导航栏和右边栏的上下文渲染器
def sidebar(request):
    # 所有标签
    tag_list = Tag.objects.all()

    # 所有文章分类
    category_list = Category.objects.all() 

    # 文章阅读量排行榜
    article_ranklist = Article.objects.all().order_by('-view')[0:6]
    
    # 轮播图
    carouselimg_list = CarouselImg.objects.all()

    return {
        'category_list': category_list,
        'article_rank': article_ranklist,
        'tag_list': tag_list,
        'carouselimg_list':carouselimg_list
    }