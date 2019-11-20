from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('blog_root')            
    else:
         form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})
