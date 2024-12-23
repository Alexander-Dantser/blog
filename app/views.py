from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from .forms import PostForm


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post(request, pk):
    post_data = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post': post_data})

def create_post(request):
    form = PostForm()
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:home')
    return render(request, 'post_form.html', {'form': form})

def edit_post(request, pk):
    post_data = Post.objects.get(id=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post_data)
    if form.is_valid():
        form.save()
        return redirect('app:post', pk=post_data.pk)
    
    
    return render(request, 'post_form.html', {'form': form})

def delete_post(request, pk):
    post_data = Post.objects.get(id=pk)

    if request.method == 'POST':
        post_data.delete()
        return redirect('app:home')
    return render(request, 'delete_post.html', {'pk': pk})
    # post_data = Post.objects.get(id=pk)
    # post_data.delete()
    # return redirect('app:home')