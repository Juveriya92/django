from django.http import HttpResponse
from .models import *
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView

from django.contrib import messages
from .forms import CreateUserForm,StoryForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def HomePage(request):
    stories=Story.objects.all()
    return render(request,'app1/home.html',{'stories':stories})

def registerPage(request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:

            form=CreateUserForm()

            if request.method=='POST':
                form=UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    user=form.cleaned_data.get("username")
                    messages.success(request, "Account is successfully created for "+ user)
                    return redirect('login')
            
        
        context={'form':form}
        return render(request, 'app1/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        context={}
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request, username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.info(request,'username or password is incorrect')

        return render(request, 'app1/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')


class Dashboard(ListView):
    model=Story
    template_name='app1/dashboard.html'
    
class StoryDetail(DetailView):
    model=Story
    template_name='app1/story_detail.html'

class UpdateStory(UpdateView):
    model=Story
    fields=['title','summary','story']
    template_name='app1/update_story.html'
    queryset=Story.objects.all()


class CreateStory(CreateView):
    model=Story
    form_class=StoryForm
    template_name='app1/add_story.html'
    queryset=Story.objects.all()
    

class DeleteStory(DeleteView):
    model=Story
    fields=['title','summary','story']
    template_name='app1/delete_story.html'
    queryset=Story.objects.all()
    success_url=('/story/userstories')
   
#

@login_required
def UserStories(request):
    user = request.user
    user_posts = Story.objects.filter(author=request.user).order_by('date_posted')
    template = 'app1/userstories.html'
    return render(request, template, {'user_posts':user_posts,'user': user})

