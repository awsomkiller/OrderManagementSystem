from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['eusername']
        password = request.POST['epassword']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            print("worked")
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            return redirect('register')
        elif password1 != password2:
            messages.info(request, 'Password did not match')
            return redirect('register')
        else:
            user = User.objects.create_user(first_name=name, username=username, email=email, password=password1)
            user.save()
            auth.login(request, user)
            return redirect('home')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
