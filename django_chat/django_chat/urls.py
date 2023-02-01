"""django_chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from chat.views import index
from chat.views import login_view, register_view, logout_view

# rename standard
admin.site.site_header = 'Chat App'     # default: "Django Administration"
admin.site.index_title = 'Structure'    # default: "Site administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', index),    
    path('login/', login_view),
    path('register/', register_view), 
    path('logout/', logout_view)
]
