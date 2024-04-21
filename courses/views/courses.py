from django.shortcuts import render , redirect
from courses.models import Course , Video , UserCourse , Quiz
from django.shortcuts import HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.db.models import Max

@method_decorator(login_required(login_url='login') , name='dispatch')
class MyCoursesList(ListView):
    template_name = 'courses/my_courses.html'
    context_object_name = 'user_courses'
    def get_queryset(self):
        return UserCourse.objects.filter(user = self.request.user)


def coursePage(request , slug):
    course = Course.objects.get(slug  = slug)
    serial_number  = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")

    if serial_number is None:
        serial_number = 1 
    max_week = Video.objects.aggregate(max_week_id=Max('week_id'))["max_week_id"]
    weeks={}
    for i in range(1,max_week+1):
        try:
            video = Video.objects.filter(course=course, week_id=i)
            quiz = Quiz.objects.filter(course=course, week_id=i)
            weeks[i] = (video,quiz)
        except Video.DoesNotExist:
            pass    
        
    context = {
        "course" : course , 
        "weeks": weeks,
        "videos" : videos,
        "slug":slug,
    }
    return  render(request , template_name="courses/course_page.html" , context=context )    

def quizPage(request,slug,week):
    course = Course.objects.get(slug  = slug)
    if request.method == 'POST':
        total_score = 0
        
        for key, value in request.POST.items():
            if key.startswith('question'):
                question_number = int(key.split('question')[1])
                
                quiz = Quiz.objects.get(serial_number=question_number, week_id=week)
                
                if int(value) == quiz.answer:
                    total_score += 1  # Increment score for correct answer
        
        context={
            "total_score" : total_score
        }
        return render(request ,"courses/quiz.html",context = context)
    
    try:
        quiz = Quiz.objects.filter(course=course, week_id=week)
    except Video.DoesNotExist:
        pass 
    context = {
        "course" : course , 
        "week" : week,
        "quizes":quiz,
    }
    return render(request ,"courses/quiz.html",context = context)