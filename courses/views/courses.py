from django.shortcuts import render
from courses.models import Course
from django.shortcuts import HttpResponse
# Create your views here.


def coursePage(request , slug):
    print(slug)
    context = {
        "slug" : slug
    }
    return render(request , template_name="courses/course_page.html" , context=context )