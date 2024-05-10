from django.shortcuts import render

# Create your views here.

def login(request):

    username=request.POST.get('username')
    password=request.POST.get('passwrord')

    print(username)

    return render(request,'login.html',{'name':'Yasser'})