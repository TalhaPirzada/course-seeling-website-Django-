from django.shortcuts import render , redirect
from django.contrib.auth import logout , login, authenticate
from courses.forms import RegistrationForm , LoginForm
from django.views import View
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

class SignupView(FormView):
    # template_name="courses/signup.html" 
    # form_class = RegistrationForm
    # success_url  = '/login'

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    template_name = "courses/signup.html"

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully. You can now log in.')
            return redirect('login')
        else:
            # If form is not valid, re-render the signup form with error messages
            return render(request, self.template_name, {'form': form})

def signup_view(request):
        if request.method=="POST":
            form=RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                username=form.cleaned_data['username']
                password=form.cleaned_data['password1']
                user=authenticate(username=username,password=password)
                login(request,user)
                messages.success(request,('Registration successful'))
                return redirect('home')
        else:
            form=RegistrationForm()
        return render(request,'courses/signup.html',{'form':form,})
            

class LoginView(FormView):
    template_name="courses/login.html" 
    form_class = LoginForm
    success_url  = '/'

    def form_valid(self, form):
        login(self.request , form.cleaned_data)
        next_page = self.request.GET.get('next')
        if next_page is not None:
            return redirect(next_page)
        return super().form_valid(form)


def signout(request ):
    logout(request)
    return redirect("home")


def login_view(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')    
        else:
            messages.success(request,('Try again, error somewhere.'))
            return redirect('login')    
            
    else:
        return render(request,'courses/login.html',{})