from django.contrib import admin
from .models import Profile

# Register your models here.
#将models注册的后台管理界面
admin.site.register(Profile)
