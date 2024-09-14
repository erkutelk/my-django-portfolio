from django.shortcuts import render, redirect       # type: ignore
from django.http import HttpResponse                # type: ignore
from django.contrib.auth import authenticate, login,logout # type: ignore

def user_login(request):
    # if request.user.is_authenticate:
    #     return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Admin_kategori_ekle')
        else:
            return render(request, 'account/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'account/login.html')

def user_logout(requset):
    logout(requset)
    return redirect('http://127.0.0.1:8000')