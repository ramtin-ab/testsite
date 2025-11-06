from django.urls import path
from blog.views import *
app_name='blog'
urlpatterns = [
    path('',blog_home,name='blog-home'),
    path('<int:pid>',blog_single,name='blog-single'),
    path('test/search/<str:name>',test,name='test'),
    path('category/<str:name>',blog_home,name='category'),
    path('author/<str:author>',author,name='author'),
    path('search/',search,name='search'),
]
