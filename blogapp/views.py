from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm
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

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, \
                             status = Post.Status.PUBLISHED)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_dataws
    else:
        form = EmailPostForm()
    return render (request, 'blogapp/email.html')