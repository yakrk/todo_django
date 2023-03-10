from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        
        # user exists?
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, 'accounts\login.html')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User already exists")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return redirect("register")
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                    )
                    user.save()
                    messages.success(request, "You are now registered")
                    auth.login(request, user)
                    return redirect ("index")
            
        else:
            #return error message
            messages.error(request, "Password does not match")
            
    return render(request, "accounts/register.html")

def logout(request):
    if request.method=="POST":
        auth.logout(request)
        messages.success(request, "You are logged out")
        return redirect ("login")
