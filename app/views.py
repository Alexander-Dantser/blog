from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})
    
    # post = Post.objects.get(id=pk)
    # return render(request, 'post.html', {'post': post})