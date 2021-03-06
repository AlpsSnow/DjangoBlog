"""DjangoBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views #django系统自带的login/logout
from django.urls import path, include
from django.conf import settings       # for upload image 只适用于开发环境
from django.conf.urls.static import static # for upload image 只适用于开发环境
from users import views as users_views  #users应用的views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',users_views.register,name='register'),  # 用户注册
    path('profile/',users_views.profile,name='profile'), # 用户profile
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),    # 用户登录
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'), # 用户注销
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'), # 请求重置密码
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'), # 执行重置密码，发送密码
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'), # 确认重置密码，设置新密码
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'), # 设置新密码完成
    path('', include('blog.urls', namespace='blog')) #默认首页 namespace='blog'指定实例名blog
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
