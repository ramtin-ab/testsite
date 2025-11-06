from django import template
from blog.models import *
register=template.Library()

@register.simple_tag(name='tedad')
def post_count():
    posts=Post.objects.filter(status=1)
    return posts 
   
@register.filter
def snippet(value,q=50):
    return value[:q]


@register.inclusion_tag('blog/popular-post.html')
def latestpost():
    posts=Post.objects.filter(status=1).order_by('published_date')[:4]

    return {'posts':posts}


@register.inclusion_tag('blog/post-category.html')
def category():
    cat={}
    categorys=Category.objects.all()
    posts=Post.objects.filter(status=1)

    for name in categorys:
        cat[name]=posts.filter(category=name).count()
  


    return {'catis':cat}