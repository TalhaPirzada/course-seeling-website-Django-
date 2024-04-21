# filter.py
from django.shortcuts import render
from courses.models import Course


def Filter(request):
    sort_by = request.GET.get('sort_by')
    courses = apply_sorting(sort_by)
    
    return render(request, 'courses/filter.html', {'courses': courses})

def apply_sorting(sort_by):
    if sort_by == 'name_asc':
        return Course.objects.all().order_by('name')
    elif sort_by == 'name_desc':
        return Course.objects.all().order_by('-name')
    elif sort_by == 'price_asc':
        return Course.objects.all().order_by('price')
    elif sort_by == 'price_desc':
        return Course.objects.all().order_by('-price')
    elif sort_by == 'date_asc':
        return Course.objects.all().order_by('date')
    elif sort_by == 'date_desc':
        return Course.objects.all().order_by('-date')
    else:
        return Course.objects.all()  
