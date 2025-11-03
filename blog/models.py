from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField()

    def __str__(self):
        return self.name



class Post(models.Model):
    title=models.CharField()
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to='blog',default='blog/default.jpg')
    content=models.TextField()
    published_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    uploaded_date=models.DateTimeField(auto_now=True)
    status=models.BooleanField()
    category=models.ManyToManyField(Category)
    counted_view=models.IntegerField(default=0)

    #def snippets(self):
        #return self.content[:100] + ' .....'

    def __str__(self):
        return self.title
    
    class Meta():
        ordering=['created_date']
        #verbose_name='پست'