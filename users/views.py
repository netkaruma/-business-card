
from django.contrib.auth import login, authenticate, logout
import json
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render,redirect

from comments.models import Comments
from users.forms import CustomUserCreationForm, CustomUserAuthForm
from django.http import JsonResponse

from users.models import CustomUser

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('main:main')

        else:
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = error_list
            request.session['form_errors'] = errors
            return  redirect('main:main')
    return redirect('main:main')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)

                return redirect('main:main')
        else:
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = error_list
            request.session['form_errors'] = errors
            return  redirect('main:main')
    
    return redirect('main:main')

def user_logout(request):
    if request.method == "POST" and request.user.is_authenticated:
        logout(request)
    return redirect("main:main")

def save_color(request):
    if request.method == "POST" and request.user.is_authenticated:
        data = json.loads(request.body)
        get_color = data.get('color')
        user = request.user
        user.color_theme = get_color
        user.save()
        print(get_color)
    
    return redirect("main:main")
        
