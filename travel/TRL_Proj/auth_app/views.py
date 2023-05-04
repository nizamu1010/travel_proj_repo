from importlib.metadata import requires
from django.contrib import messages ,auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
        
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        u_name = request.POST['username']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        mail = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 == pass2:

            if User.objects.filter(username=u_name).exists():
                messages.info(request, "Username taken.")
                return redirect('signup')
            elif User.objects.filter(email=mail).exists():
                messages.info(request, "email taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=u_name, first_name=f_name, last_name=l_name,
                                                password=pass1, email=mail)
                user.save()
                return redirect('login')

            # print('user created')

        else:
            messages.info(request, 'password is not matched')
            return redirect('signup')

        return redirect('/')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
    


