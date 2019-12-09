from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse   # URL反向函数，返回一个绝对地址的URL字符串

# Create your models here.

class Tag(models.Model):
    name = models.CharField(u'文章标签', max_length=30)

    class Meta:        
        verbose_name = u"文章标签"   #模型类的可读名称
        verbose_name_plural = verbose_name  #模型类的可读名称的复数形式 eg. xxx+s

    def __str__(self):
        """
        返回model对象自身
        """
        return self.name

class Category(models.Model):
    name = models.CharField(u'文章类型', max_length=30)

    class Meta:
        ordering = ['name']         #排序
        verbose_name = u"文章类型"   #模型类的可读名称
        verbose_name_plural = verbose_name  #模型类的可读名称的复数形式 eg. xxx+s

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(verbose_name=u'标题',max_length=200)    #文章标题
    digest = models.TextField(verbose_name=u'摘要', blank=True, null=True)  # 文章摘要
    picture = models.CharField(max_length=200)  # 文章标题的配图地址
    content = models.TextField(verbose_name=u'正文', blank=True, null=True)  # 正文
    created_date = models.DateField(verbose_name=u'创建日期',auto_now_add=True)  # 博客创建日期
    last_mod_date = models.DateTimeField(auto_now=True) # 博客修改日期
    author = models.ForeignKey(User, verbose_name=u'作者', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=u'类型', on_delete=models.CASCADE)  #分类，一对一
    tag = models.ManyToManyField(Tag,verbose_name=u'标签')  # 标签，多对多
    view = models.BigIntegerField(verbose_name=u'阅读量',default=0)  # 阅读数
    comment = models.BigIntegerField(verbose_name=u'评论数',default=0)  # 评论数

    class Meta:  # 按时间降序
        ordering = ['-created_date']
        verbose_name = u"文章"   #模型类的可读名称
        verbose_name_plural = verbose_name  #模型类的可读名称的复数形式 eg. xxx+s

    def __str__(self):
        return self.title
    
    def viewed(self):
        """
        增加阅读量函数
        """
        self.view += 1
        self.save(update_fields=['view'])
    
    def commenced(self):
        """
        增加评论数
        :return:
        """
        self.comment += 1
        self.save(update_fields=['comment'])
    
    # 给通用模板处理返回一个绝对地址的URL字符串
    # 发布博文后，应用会自动重定向到该URL
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

class CarouselImg(models.Model):
    title = models.CharField(verbose_name=u'标题', max_length=200)    # 轮播图的标题    
    #上传路径到：carousel_pics
    image = models.ImageField(verbose_name=u'图片', upload_to='carousel_pics') # 轮播图

    class Meta:
        verbose_name = u"轮播图"   #模型类的可读名称
        verbose_name_plural = verbose_name  #模型类的可读名称的复数形式 eg. xxx+s
    
    def __str__(self):
        return self.title
