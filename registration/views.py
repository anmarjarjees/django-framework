from django.shortcuts import render

# Create your views here.

# We need to import the class "HttpResponse" from "django.http" module for now just to test our pages
# we use this class as a temporary solution to test our views functions
# instead of using render templates function 
# becasue we don't have our templates (html pages) created yet
# we don't have templates folder with any HTML page to be renderd!
# for this reason, we just need to dispaly a simple text
# to skip all these steps and just to test our links to have something to be displayed we used "HttpResponse"
from django.http import HttpResponse

# Any html page (template) you want to display/render 
# has to have its own function defined in this file "views.py":
# starting with the first page "home page"
# def home() ==> for the home page
# As a rule for Django, every view function below has to have an argument called "request"
def home(request):
    # In Django, we cannot just return a simple text value!
    # since we are sending a request as an argument for any view function
    # We have to use HTTP Response return with the return statement
    # in Django we have a class called "HttpResponse" that we we can use:
    # the template: return HTTPResponse("<h1>Wellcome to our Home page!!!</h1>")
    # or just use single quote
    return HttpResponse('<h1>Wellcome to our Home page!!!</h1>')

def about(request):
    return HttpResponse('<h1>About Us</h1>')

def contact(request):
    return HttpResponse('<h1>Contact Us</h1>')
