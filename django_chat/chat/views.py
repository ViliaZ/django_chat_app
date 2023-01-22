from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Chat, Message
from django.http.response import HttpResponseRedirect


# Create your views here.

@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        print('erfolgreich gesendet ' + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages})
 
def login_view(request):
    # dynamic redirection -> get the value of the query parameter 'next' from url, e.g. /chat/  
    redirect = request.GET.get('next')
    print(redirect)
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            # get value of hidden input field "redirect"
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            return render(request, 'auth/login.html', {'wrong_password': True}, {'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})
    