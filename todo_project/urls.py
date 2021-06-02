"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from todo.views import logoutuser, signupuser, currenttodos, home, loginuser, createtodo, viewtodo, completetodo, deletetodo, completedtodos

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('signup/', signupuser, name='signupuser'),
    path('logoutuser/', logoutuser, name='logoutuser'),
    path('loginuser/', loginuser, name='loginuser'),

    path('currenttodos/', currenttodos, name='currenttodos'),
    path('createtodo/', createtodo, name='createtodo'),
    path('completedtodos/', completedtodos, name='completedtodos'),
    path('todo/<int:todo_pk>', viewtodo , name='viewtodo'),
    path('todo/<int:todo_pk>/complete', completetodo , name='completetodo'),
    path('todo/<int:todo_pk>/complete', deletetodo , name='deletetodo'),
]
