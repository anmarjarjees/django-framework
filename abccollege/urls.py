"""abccollege URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

# We need/have to import the file "views.py" into this file "urls.py"
# Based on the instructions in the Django comment (above):  from my_app import views
# we need to import the views:
# You might not have any view created yet, but we will add them inside the registration app folder
# Our current applicatin name is "registration"
from registration import views
# we can just write: from . import views (. refers to any app name)




# Django gave us the "ulrpartterns" => urlpatterns = [path('admin/', admin.site.urls),]
# urlpatterns for specify all the url links
# urlpatterns = [ path(arguments), path(arguments), path(arguments),]
# We will our custom paths to this list
urlpatterns = [
    # you can see below the default Django code for admin path
    # and that's why we were able to access the admin page by typing: http://localhost:8000/admin 
    path('admin/', admin.site.urls),

    # Every page (template) you need to render/dispaly, has to have its path() function
    # the number of path() functions will be the same number for the pages you want to visit
    # Like Flask Framework: every page has a function to render it
    # then below we will add our own custom path functions:

    # path() function#1: 
    # This function just for rendering the home page
    # the url: http://127.0.0.1:8000/
    # for the empty path (the root url) => load the home function (views.home) from the views module 
    # the pattern name is home: name='home'
    # name='home' will be used when we create the link dyncmicaly to reference this page
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
]
