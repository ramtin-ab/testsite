from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'website/index.html')

def about(request):
    return render(request,'website/about.html')

def contact(request):
    return render(request,'website/contact.html')

def test(request):
    context={'name':'ramtin','age':'23'}
    return render(request,'website/test.html',context)
