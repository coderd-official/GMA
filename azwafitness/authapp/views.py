from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Contact

# login required decorator
from django.contrib.auth.decorators import login_required

# unauthenticaed user decorator



# Create your views here.
def Home(request):
    return render(request,"index.html")

def services(request):
    context={}
    return render(request,"services.html",context)


@login_required
def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
   
    return render(request,"profile.html")


def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
      
        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
       
        try:
            if User.objects.get(username=username):
                messages.warning(request,"User already exists.")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email address already taken.")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"Your account created successfully!")
        return redirect('/login')
        
        
    return render(request,"signup.html")


def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            return redirect('/profile')
        else:
            messages.error(request,"Username or Password incorrect")
            return redirect('/login')
            
        
    return render(request,"handlelogin.html")


def handleLogout(request):
    logout(request)
    return redirect('/login')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        myquery=Contact(name=name,email=email,subject=subject,message=message)
        myquery.save()       
        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/contact')
        
    return render(request,"contact.html")

