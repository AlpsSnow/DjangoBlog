from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    #一对一，一个profile对应一个User，并指明用户删除同时删除profile，
    # 但是profile删除不会删除User（这是单方向的）
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #默认头像：default.jpg
    #上传路径到：profile_pics
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    #print用
    def __str__(self):
        return f'{self.user.username} Profile'

