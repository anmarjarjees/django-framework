# Django is importing render module for us:
# the "render" module will be used to render our html templates
from django.shortcuts import render

# Create your views here.

# We need to import the class "HttpResponse" from "django.http" module for now just to test our pages
# we use this class as a temporary solution to test our views functions
# instead of using render templates function 
# because we don't have our templates (html pages) created yet
# we don't have templates folder with any HTML page to be renderd!
# for this reason, we just need to display a simple text
# to skip all these steps and just to test our links to have something to be displayed we used "HttpResponse"
from django.http import HttpResponse

# Any html page (template) you want to display/render 
# has to have its own function defined in this file "views.py":
# starting with the first page "home page"
# def home() ==> for the home page
# As a rule for Django, every view function below has to have an argument
# This argument will represent the HTTP request to be sent to the server
# And that's why we can call it "request" by convention
# yes, we can call it anything we want as a simple python function
# if we don't specify => Error: home() takes 0 positional arguments but 1 was given
def home(request):
    # In Django, we cannot just return a simple text value!
    # since we are sending a request as an argument for any view function
    # We need this function to return just a simple text as a response just for testing
    # We have to use HTTP Response return with the return statement
    # in Django we have a class called "HttpResponse" that we we can use:
    # the template: return HTTPResponse("<h1>Wellcome to our Home page!!!</h1>")
    # or just use single quote
    return HttpResponse('<h1>Wellcome to our Home page!!!</h1>')

# def about ==> for the about us (me) page
# about function has the required argument "request" and so on for all the functions
def about(request):
    return HttpResponse('<h1>About Us</h1>')

def contact(request):
    return HttpResponse('<h1>Contact Us</h1>')

# def student_detail ==> for the student detail page
# this function requires the Student ID as a second parameter
def student_detail(request, student_id):
    # Either this way:
    # return HttpResponse('<h1>Student Detail for id = ' + str(student_id) +'</h1>')
    # Or this one "f fromat string":
    return HttpResponse(f'<h1>Student Detail for id {student_id} </h1>')

# *************************************************************
# Notice that these two functions (views) are not being called
# because we didn't add a path() function for each one inside urls.py
def services(request):
# if the fucntion is completely empty => ErrorIndentationError: expected an indented block
# In such case we can use the same keyword "pass" that we used when we created an empty class
    pass

def products(request):
# Or we can just let this function returns anything:
    return True
