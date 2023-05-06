from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

'''Funcion que muestra el  Index'''
def index(request):
    posts_list = Post.published.all()
    paginator = Paginator(posts_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
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
