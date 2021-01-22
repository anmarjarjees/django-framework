# Django is importing render module for us:
# the "render" module will be used to render our html templates
from django.shortcuts import render

# Create your views here.

# We will need to import the class "Student" to access all student records in the database:
# So we can use the same statement that we used before with ORM and Python Shell
# being very specific by writing the applicating name
# from registration.models import Student 
# Or we can just use .models to refer to any application name
from .models import Student # with capital S for Student because it's a class
# Then we can use the Student model to make queries against the student table 

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
    # In the home page, we will display all the students record (from our database)!
    # this function main job is to query the database table(s)
    # We need to get all the records from the database:
    # Yes, we will use again: Query data with the Django ORM (Object Relational Mapper) 
    # We used [Python Shell] to practise these commands
    # We used: Student.objects.all() => display all the instances of this model (class: Student)
    # This "home" function should use the same Django ORM to fetch all the records
    # we will start with a query for all the students
    # we will use the same command that we learnt before inside the project Py shell window
    # (refer to my ORM topic in the pdf file)
    # and we can assign the result of all these objects into a variable:
    students = Student.objects.all()  # This command will grab all the objects in our student table
    # Note: We will have this Error: name 'Student' is not defined
    # If we don't import the class "Student"
    return render(request,'home.html',
    { 
        'first_h1':'Welcome to Django! Your way to go',
        'students': students,
    })

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
    # run the query for that specific student based on its id number:
    # We need to write the same queries against our database!
    # We can just go to review the "ORM commands" in the in-class notes and that's it 
    # The same commands we can just place them here:

    student = Student.objects.get(id=student_id)
    
    # assuming we have only 20 students, if the id is > 20 => "Student not found!"
    # if student_id > 20:
        # we need to return 404 explicitly from Django (Not the default 404 of the browser)
        # Since we imported the class "Http404" 
        # we can use it to raise an error message with any string we want
        # using the built-in raise function with the class "Http404"
        # HTTP404('Any message you want')
    #    raise Http404('Sorry, student not found!')





    return render(request,'student_detail.html',{'student': student})

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
