from django.shortcuts import render, redirect
from .forms import RegisterForm,Profile
from django.contrib.auth.views import LoginView,PasswordChangeView
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

# Create your views here.
@unauthenticated_user
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form":form})

@unauthenticated_user
def custom_login_view(request, *args, **kwargs):
    return LoginView.as_view()(request, *args, **kwargs)

@login_required(login_url='login')
def custom_password_change(request,*args, **kwargs):
    return PasswordChangeView.as_view()(request,*args, **kwargs)

############
@login_required(login_url='login')
def main(request):
    return render(request,"main/main.html")
############

@login_required(login_url='login')
def view_profile(request):
    context = {
        'user' : request.user
    }
    return render(request, 'main/view_profile.html',context)
