from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_user, logout



def layout(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_user(request, user)
            return redirect('index')

    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')