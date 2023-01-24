from sqlite3 import dbapi2
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Chat, Message
from django.http.response import HttpResponseRedirect

@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        print('erfolgreich gesendet ' + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})
 
def login_view(request):
    # dynamic redirection -> get the value of the query parameter 'next'
    # Goal: user get redirected to his original chosen page (dynamic!), after success login
    redirect = request.GET.get('next')
    print(redirect)
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:    
            login(request, user)
            if redirect == None: 
                return HttpResponseRedirect('/chat')
            # in case user has previously clickt an url, redirect to query parameter "?next="
            else:
                return HttpResponseRedirect(request.POST.get('redirect'))
            # in case there is no "next" parameter in the url, redirect to chat directly
        else:
            return render(request, 'auth/login.html', {'wrong_password': True, 'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('passwordvalue1')
        password2 = request.POST.get('passwordvalue2')

        existing_user = User.objects.filter(username=username).exists()
        
        if existing_user:
            return render(request, 'auth/register.html', {'error_message': 'Username is already taken.'})
        if password1 != password2:
            return render(request, 'auth/register.html', {'error_message': 'Passwords do not match.'})
        else:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            return redirect('/login')
    return render(request, 'auth/register.html')