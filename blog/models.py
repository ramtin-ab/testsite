from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField()
    content=models.TextField()
    published_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    uploaded_date=models.DateTimeField(auto_now=True)
    status=models.BooleanField()
    counted_view=models.IntegerField(default=0)


    def __str__(self):
        return self.title
    
    class Meta():
        ordering=['created_date']
        #verbose_name='پست'