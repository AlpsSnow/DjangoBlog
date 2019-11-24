from django.shortcuts import render,redirect
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm #django默认注册用户的form
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #判断表单数据是否正确
        if form.is_valid():
            form.save() #将注册的用户保存到数据库
            username = form.cleaned_data.get('username') #取得表单的username           
            messages.success(request,f'Account created for { username }!')
            return redirect('blog:index')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})
