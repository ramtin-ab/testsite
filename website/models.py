from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField()
    subject=models.CharField()
    email=models.EmailField()
    message=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta():
        ordering=['created_date']