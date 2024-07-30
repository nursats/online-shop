from django.shortcuts import render

# Create your views here.
def login(request):
    context = {
        'tilte':'Home - Авторизация',
    }
    
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'tilte':'Home - Регистрация',
    }

    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'tilte':'Home - Кабинет',
    }

    return render(request, 'users/profile.html', context)

def logout(request):
    ...