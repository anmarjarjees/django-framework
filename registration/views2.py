# Django is importing render module for us:
# the "render" module will be used to render our html templates
from django.shortcuts import render

# Create your views here.

# We need to import the class "Http404" from "django.http" module
# we use this class to let Django generate its own "404 page not found" error
# This class we needed for the wrong url
# Just an extra good feature if you want to add to your project
from django.http import Http404


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
    # render() method:
    # First Argument: request object is the first needed argument for the render() function 
    # this argumetn request will be used again to send a request to render the required page
    # Second Argument: is the name of the HTML template we want to use
    # Third Argument [Optional]: the dictionary for the data to put in the template or to pass to the template
    # the keys of this dictionary will be string variables 
    # in this example we will use the key 'students' with the value of students variable
    # render(request: HttpRequest, template_name, { could be empty OR anything we want to pass to this page } )
    # { } <= If they are empty we can just ignore them
    # Pattern: { 'feild1': numeric_value, 'feild2': 'text_value', 'field3': variable_name }
    # We can name the home page index.html as we used to do pure html
    # But with Flask/Django we can name it anything

    # In Flask:
    # return render_template("index.html", page_title="Our Program")
    # In Django:
    # return render ("index.html", 'page_title':'Our Program')
    return render(request,'home.html',{ 'first_h1':'Welcome to Django! Your way to go'})

# def about ==> for the about us (me) page
# about function has the required argument "request" and so on for all the functions
def about(request):
    module_name="Learning Django Framework"
    course_list = ['HTML and CSS','Bootstrap','JavaScript','Python','Flask Framework','Django Framework']
    # In Python we can use type() function to return the data type of the value any variable:
    var_type = type(course_list)
    return render(request,'about.html',
    {
     'language':'Python',
     'module':module_name,
     'module_id':11,'is_easy':True,
     'course_list':course_list,
     'var_type':var_type
    })

def contact(request):
    return render(request,'contact.html')

# def student_detail ==> for the student detail page
# this function requires the Student ID as a second parameter
def student_detail(request, student_id):
    # assuming we have only 20 students, if the id is > 20 => "Student not found!"
    if student_id > 20:
        # we need to return 404 explicitly from Django (Not the default 404 of the browser)
        # Since we imported the class "Http404" 
        # we can use it to raise an error message with any string we want
        # using the built-in raise function with the class "Http404"
        # HTTP404('Any message you want')
        raise Http404('Sorry, student not found!')

    return render(request,'student_detail.html',{'student_id': student_id})

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
