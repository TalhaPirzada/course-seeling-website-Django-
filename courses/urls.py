
from django.contrib import admin
from django.urls import path , include
from courses.views import  MyCoursesList,  HomePageView ,verifyPayment ,  coursePage , SignupView , LoginView , signout , checkout, search_view,Filter,quizPage,login_view,about_us,blog,signup_view
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', HomePageView.as_view() , name = 'home'),
    path('search',search_view,name='search'),
    path('logout', signout , name = 'logout'),
    path('my-courses', MyCoursesList.as_view() , name = 'my-courses'),
    path('signup', signup_view , name = 'signup'),
    path('login', login_view , name = 'login'),
    path('course/<str:slug>', coursePage , name = 'coursepage'),
    path('check-out/<str:slug>', HomePageView.as_view() , name = 'check-out'),
    path('course/<str:slug>/quiz/<int:week>/',  quizPage, name = 'quiz'),
    path('verify_payment', HomePageView.as_view() , name = 'verify_payment'),
    path('filter',Filter,name='filter'),
    path('about',about_us,name='about'),
    path('blog',blog,name='blog'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)