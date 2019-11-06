from django.db import models
from django.contrib.auth.models import User

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
    title = models.CharField(max_length=200)    #文章标题
    digest = models.TextField(blank=True, null=True)  # 文章摘要
    picture = models.CharField(max_length=200)  # 文章标题的配图地址
    content = models.TextField(blank=True, null=True)  # 正文
    created_time = models.DateField(auto_now_add=True)  # 博客创建日期
    last_mod_time = models.DateTimeField(auto_now=True) # 博客修改日期
    author = models.ForeignKey(User, verbose_name=u'作者', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=u'文章类型', on_delete=models.CASCADE)    
    tag = models.ManyToManyField(Tag,verbose_name=u'文章标签')  # 标签 
    view = models.BigIntegerField(default=0)  # 阅读数
    comment = models.BigIntegerField(default=0)  # 评论数

    class Meta:  # 按时间降序
        ordering = ['-created_time']
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
