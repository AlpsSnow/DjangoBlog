from django.db import models
from django.contrib.auth.models import User
from PIL import Image  # 创建缩略图用

class Profile(models.Model):
    #一对一，一个profile对应一个User，并指明用户删除同时删除profile，
    # 但是profile删除不会删除User（这是单方向的）
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #默认头像：default.jpg
    #上传路径到：profile_pics
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    # print用
    def __str__(self):
        return f'{self.user.username} Profile'

    # 重写父类（models.Model）的save的方法，用来保存上传图片的缩略图
    def save(self, force_insert=True, using=None):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:            
            output_size = (300, 300) 
            img.thumbnail(output_size)          
            img.save(self.image.path)
            
