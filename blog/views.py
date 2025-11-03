from django.shortcuts import render,get_object_or_404
from blog.models import *
# Create your views here.
def blog_home(request):
    posts=Post.objects.filter(status=1)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)



def blog_single(request,pid):
    posts=Post.objects.filter(status=1)
    # rahe 2  post=get_object_or_404(posts,id=pid,status=1)
    post=get_object_or_404(posts,id=pid)
    context={'post':post}
    return render(request,'blog/blog-single.html',context)


def test(request):
    posts=Post.objects.get(id=1)
    context={'posts':posts}
    return render(request,'website/test.html',context)