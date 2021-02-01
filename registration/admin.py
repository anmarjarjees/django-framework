# The first line just to import the admin module
# that we will use below (Written By Django)
from django.contrib import admin

# Register your models here.
# **************************

# Embed/Insert the Student Model (Class) and the Workshop Model (class)
# from models.py file (which is inside the same folder)
from .models import Student, Workshop
# NOTE:
# Using: from models
# will give us this error: ModuleNotFoundError: No module named 'models'
# Solution: we have to write: from .models
# So please don't forget to add the dot before models


# Make an admin interface for Student model:

# We need register this class with the admin to identify its associated model
# We will need to use a decorator from the admin model called "register"
# like "@admin.register(Student)":
# this decorator is from the admin model
# this decorator is called "register"
# this decorator takes our model classes and arguments
# Here is the code: @admin.register(Student) <== to be added above the class directly
@admin.register(Student)  # <= using the decorator "register"
# We need to create a class and let's name it "StudentAdmin"
# that inherits from admin.ModelAdmin:
# As you remember in our basic example class Basic_Member(Member) :-)
class StudentAdmin(admin.ModelAdmin):
    # class can have attributes (class fields/variable) and methods (class functions)
    # Which means the class does need at least one line of code to work
    # so to make this a valid Python class we will add this line using the "pass" keyword
    pass  # <= I will comment "pass" because I will add some code below
    # Now we need to comment/delete pass to continue our code

    # First Problem: Each Student is displayed as Student (Object #)
    # Although we fixed this problem by modifying the method __str__(self) inside the class "Student"

    # But we can also another more advanced solution to enhance the look/layout of page:
    # The model admin class has an attribute (built-in field) called "list_display":
    # This attribute:
    # Allows us to define which field are displayed on this listing screen
    # It works like a simple python list (array)

    # inside this list (array) we will list the string names for all the fields
    # that we want to display in the admin list page:
    # NOTES:
    # 1. We have to use the field names exactly as we used in the class "Student" in the models.py file
    # 2. We can include the Many-To-Many Field in this list (Which is in our case it's "workshops" field)
    # 3. We don't have to list all the fields! We can pick some of them:
    list_display = ['first', 'last', 'program_category', 'course', 'course_description',
                    'average', 'gender', 'graduation_date', 'last_modified_date']


@admin.register(Workshop)  # <= using the decorator "register"
# We need to create another class and let's name it "WorkshopAdmin"
# that inherits from admin.ModelAdmin:
class WorkshopAdmin(admin.ModelAdmin):
    # Review: aging don't forget to put "pass"  => SyntaxError: unexpected EOF while parsing
    pass
