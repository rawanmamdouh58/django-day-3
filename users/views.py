from django.shortcuts import render ,redirect

# Create your views here.


def login(requset):
    return render(requset,'login.html')

def logout(requset):
    return render(requset,'logout.html')

def register(requset):
    return render(requset,'register.html')