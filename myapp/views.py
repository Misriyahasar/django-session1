from django.shortcuts import render,redirect
from django.conf.urls import url
from django.http.response import HttpResponse
from myapp.forms import LoginForm

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        full_name = request.POST['full_name']
        gender = request.POST['gender']
        age = request.POST['age']

        request.session['email'] = email
        request.session['full_name'] = full_name
        request.session['gender'] = gender
        request.session['age'] = age

        return render(request, 'myapp/profile.html')
    else:
        return render(request, 'myapp/login.html')
        
def profile(request):
    if 'email' in request.session:
        email = request.session['email']
        full_name = request.session['full_name']
        gender = request.session['gender']
        age = request.session['age']

        return render(request, 'myapp/profile.html', {
            'email': email,
            'full_name': full_name,
            'gender': gender,
            'age': age
        })
    else:
        return render(request, 'myapp/login.html')

def logout(request):
    request.session.clear()
    return render(request, 'myapp/login.html')
