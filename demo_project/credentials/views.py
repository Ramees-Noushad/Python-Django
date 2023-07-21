from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials!!')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method== 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Taken!! \n Please try Another Username ')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'E-mail Already Taken!! \n Please try with Another E-mail ')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                return redirect('login')
                
        else:
            messages.info(request,'Password Mismatch!! \n Please try another one')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')