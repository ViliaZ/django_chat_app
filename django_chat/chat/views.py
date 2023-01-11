from django.shortcuts import render

# Create your views here.


def index(request):
    if request.method == 'POST':
        print('erfolgreich gesendet ' + request.POST['textmessage']) 
    return render(request, 'chat/index.html', {"name": "Vilia"})