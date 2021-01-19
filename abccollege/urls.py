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
# Our current application name is "registration"
from registration import views
# Or we can just write: 
# from . import views 
# (. refers to any app name)

# In registration (App name)/urls.py
# a variable "urlpatterns" as a one word and all in lower case
# Django gave us this "ulrpartterns" => urlpatterns = [path('admin/', admin.site.urls),]
# urlpatterns => list of calls to the path() functions, path function will
# - specify all the url links
# - all the related views (functions to render the html templates)
# urlpatterns = [ path(arguments), path(arguments), path(arguments),]

# The path function arguments (pattern):
# 1) Path Converter [Required]: the url parameters or pattern string, example: /admin or /about
# 2) View [Required]: The required view function inside (views.py)
# 3) Name [Optional for testing the links with using address bar, but it's required when using navigation]:
#    Name: name=the requird view function which is used to create links with templates

# When a request comes, Django will check the list of the path function
# to check which one will match the request:
# We will our custom paths to this list

# Even in Django Comment above:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
urlpatterns = [
    # you can see below the default Django code for admin path [We don't change it!]
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
    # name='home' will be used when we create the hyperlink dyncmicaly to reference this page
    path('', views.home, name='home'),
    # To clarify the above first function: path('', views.home, name='home')
    # The first argument '' empty which means nothing extra in the url just the site basic address
    # The second argument views.home to tell Django which view (function) to call when the URL is empty
    # the third argument name='home' is the path definition to be used with hyperlinks html elements 

    # path() function#2: 
    # This function just for rendering the about page
    # the url: http://127.0.0.1:8000/about
    # again name='about' will be used when we create the link dyncmicaly to reference this page
    path('about/', views.about, name='about'),

    # path() function#3: 
    # This function just for rendering the about page
    # the url: http://127.0.0.1:8000/contact
    path('contact/', views.contact, name='contact'),

    # path() function#4:
    # To recap from Flask we used => @app.route("/about/<var_name>")
    # But in Django we use => 'app_name/<data type:var_name>'
    # for our app => registration/<int:student_id>
    # So let's name our var_name that will reprsent the id for the student to x
    # NOTE: the varibale name we use here has to be the same varaible name we pass to the view function
    # In other word:
    # a route for looking at individual student to display his/her full details info
    # Like Django Admin URL Link: http://127.0.0.1:8000/admin/registration/student/3/change/
    # Our URL Link: http://127.0.0.1:8000/registration/1 ==> show the details of student with id=1
    # We need to translate this URL "/registration/1" into the path pattern "/registration/student_id":
    # registration/ <= the application folder
    # Using angle brackets <> to create the "Capture Group" <int:student_id>
    # The symbols  < > => anything inside this symbol is called "Capture group"
    # int the type of the variable then : then the variable name "student_id"
    # int is short for intiger which is the "converter type" 
    # to tell Django that it should be a number like registration/1 or /2 or etc..
    # we end our patterns with / to mark the end of the pattern in Django
    # load the student_detail function that accept the argument "student_id" to load the details for that student 
    # The Capture Group Pattern: <data_type: variable_name>
    path('registration/<int:student_id>/', views.student_detail, name='student_detail'),
]
