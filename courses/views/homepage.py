from courses.models import Course
from django.views.generic import ListView
from courses.forms import searchForm
class HomePageView(ListView):
    template_name = "courses/home.html"
    queryset = Course.objects.filter(active=True)
    context_object_name = 'courses'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = searchForm(self.request.GET)
        if 'query' in self.request.GET:
            query = self.request.GET['query']
            context['results'] = Course.objects.filter(name__icontains=query)
        return context
    

