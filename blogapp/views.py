from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
# Create your views here.

'''Funcion que muestra el  Index'''
def index(request):
    posts = Post.published.all()
    return render(request,
                                "./blogapp/base.html",
                                 {'posts': posts})

def post_detail(request,id):
    post = get_object_or_404(Post,
                                                        id=id,
                                                        status = Post.Status.PUBLISHED)
    return render(request,
                                './blogapp/detail.html',
                                {'post': post})
