from django.shortcuts import render

def about_us(request):
    return render(request,'courses/AboutUs.html')

def blog(request):
    return render(request,'courses/Blog.html')