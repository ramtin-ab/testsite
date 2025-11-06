from django.shortcuts import render,get_object_or_404
from blog.models import *
# Create your views here.
def blog_home(request,name=None):
    if name!=None:
        posts=Post.objects.filter(status=1)
        posts=posts.filter(category__name=name)
    else:
        posts=Post.objects.filter(status=1)

    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)


def blog_single(request,pid):
    posts=Post.objects.filter(status=1)
    # rahe 2  post=get_object_or_404(posts,id=pid,status=1)
    post=get_object_or_404(posts,id=pid)
    context={'post':post}
    return render(request,'blog/blog-single.html',context)


def test(request,name=None):

    posts=Post.objects.filter(status=1)
    if name!=None:
        posts=posts.filter(content__contains=name)
    context={'posts':posts}
    return render(request,'blog/test.html',context)
   


def author(request,author):
    posts=Post.objects.filter(status=1)
    posts=posts.filter(author__username=author)
    context={'posts':posts}

    return render(request,'blog/blog-home.html',context)


def search(request):
    posts=Post.objects.filter(status=1)
    q=request.GET.get('q')
    posts=posts.filter(content__contains=q)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
