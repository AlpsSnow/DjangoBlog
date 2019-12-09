from django.shortcuts import render,redirect
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm #django默认注册用户的form
from django.contrib import messages
from django.contrib.auth.decorators import login_required #只有已经登录的用户才能访问视图
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #判断表单数据是否正确
        if form.is_valid():            
            form.save()     #将注册的用户保存到数据库
            username = form.cleaned_data.get('username') #取得表单的username           
            messages.success(request,f'成功创建账号 { username } !')
            messages.info(request,f'你现在可以去登录了！')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

#用户必须login之后才能进入这个视图
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'个人信息更新成功！')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context ={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'users/profile.html',context)
