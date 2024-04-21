from django.shortcuts import render 
from courses.models import Course
from courses.forms import searchForm

def search_view(request):
    form = searchForm(request.GET)
    results = []
    if form.is_valid():
        query = form.cleaned_data.get('query')
        results = Course.objects.filter(name__icontains=query)
    return render(request, "courses/search.html", {'form': form, 'results': results})