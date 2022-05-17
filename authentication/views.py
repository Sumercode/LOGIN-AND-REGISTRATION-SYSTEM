from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, "authentication/index.html")


def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        email = request.POST['email']
        passwd = request.POST['passwd']
        confirmpass = request.POST['confirmpass']

        if User.objects.filter(username=username):
            messages.error(
            request, "Username already exist! Please try some other username.")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')

        if passwd != confirmpass:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')

        myuser = User.objects.create_user(username, email, passwd)
        myuser.first_name = fname
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!")

        return redirect('signin')

    return render(request, "authentication/signup.html")




def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        passwd = request.POST['passwd']

        user = authenticate(username=username, password=passwd)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/homepage.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credentials ! ")
            return redirect('home')

    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')
