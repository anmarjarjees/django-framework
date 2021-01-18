from django.db import models
# Above is the base class of django.db called "models"
# We need to inherit from for each model we define below

# Create your models here.

# Note to remember:
# Each class we create inside this file "models.py" 
# refers to a table in our default database "db.sqlite3"
# remember in our lecture we used this example for inhertance: class Basic_Member(Member):

# Creating our class to cotain the required information for/about each student
class Student(models.Model):
    
    # first field for saving the first name of the student
    first = models.CharField(max_length=40)

    # last field for saving the last name of the student
    last = models.CharField(max_length=40)
    
    # program_category field for saving the program name:
    # for example in our college we have the following programs:
    # Business Programs
    # Information Technology Programs
    # Marketing Programs

    # Each Program from the above list can have different courses:
    # for example, IT Programs include the following courses:
    # Database Administrator 
    # Full Stack Software Developer (FSSD)
    # Network Engineering
    # Software Engineering
  
    # blank = True => not a required field (We can leave it empty and db.sqlite3 will not complaint)
    program_category = models.CharField(max_length=35, blank=True) # Optional Field (could be empty)

    # course field for saving the course name (course name is mandetory, cannot be empty)
    course = models.CharField(max_length=40)

    # A brief info/description about the course
    course_description = models.TextField(blank=True)

    # Gender can be "M" for Male or "F" for Female which is only one Character 
    # so we can set its max length to 1
    # since we have a limited choices either M or F, we can use the choices field attribute
    # for more info: https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices

    # Step1: Create our choise tuple:
    # Creating a Constant to be used for the Gender field:
    # In Python (like other languages) Constant are written all in upper case as we learnt before
    # This Gender constant has only two choices: F or M
    # The choices values are just a python list [ ]
    # Each choice is a two tuple:
    # tuple => ('value1','value2')
    # the full list => [('value1','value2'),('value2','value3'), etc...]
    ## The first value is what is stored in the database => either M or F
    ## The second value is used as a display string in forms and Django Admin => either Male or Female
    GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ]

    # If we don't know the gender, we can leave the field empty => blank=True
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES, blank=True) # New concept!

    # graduation_date:
    # We will NOT use DateTimeField() because it will force us to insert the time also!
    # Who wants to enter the time for graudation!!! :-)

    # Instead we will use  DateField()
    # DateField can have one of the following optional attributes at a time:
    # auto_now=True => will set the date for any new record (student) to the current date 
    # auto_now_add=True => for setting and adding date
    
    # Note: We cannot use the two attributes together at the same time for the same field
    # if we use them both and run the command: py manage.py showmigrations 
    # ERRORS:
    # registration.Student.graduation_date: (fields.E160) The options auto_now, auto_now_add, and default are mutually exclusive. Only one of these options may be present.
    
    # To read more about DateField or DateTimeField: 
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.DateField
    # check for another option named default
    # Using this attribute: auto_now_add=True ==> will make the Date field invisible for adding/modifying
    # We left it empty to put the date by ourselves
    graduation_date = models.DateField()

    # Created or Update Date Field just for the admin(s) [Not for the end user]
    # To know when does this record updated or inserted or created
    # Using this attribute: auto_now=True ==> will make the Date field invisible for adding/modifying
    # Django will insert the current date automatically
    last_modified_date = models.DateField(auto_now=True)

    # average field for the final average
    # The FloatField the DecimalField class. 
    # They both represent real numbers, they represent those numbers differently. 
    # FloatField uses Python’s float type internally, 
    # while DecimalField uses Python’s Decimal type. 
    # for more info: 
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/#floatfield

    # Using blank=True or using null=true
    # using blank=True (optional) with numeric fields the value will be saved as 0 
    # using null=True (optional) with numeric fields will have no value "null" to make it clear that it's unknown
    # just for the learning purpose we you can to try to add null and remove it later

    # To work with DecimalField => 
    # We have two mandetory/required attributes: max_digit and decimal_places
    ## DecimalField is a field which stores a fixed-precision decimal number, 
    ## represented in Python by a Decimal instance.
    ## The following two attributes are required:
    ### max_digits attribute
    ### decimal_places attribute
    ## Examples:
    ## Number: 99 => max_digits=2 and decimal_places=None
    ## Number: 99.78 => max_digits=4 and decimal_places=2
    ## Number: 999.857 => max_digits=6 and decimal_places=3 
    ## maybe we might have this average: 100.00!!!!
    average=models.DecimalField(max_digits=4, decimal_places=2, null=True)
    # if you want it to be an integer data type field: models.IntegerField(null=True)
    # For more info: https://www.geeksforgeeks.org/decimalfield-django-models/

    # To recap/review:
    # In sql dabatase, we can have relations between tables:
    # 1 to many
    # many to many => this one reflects our connection between the studend and the workshop
    # 1 to 1 (rare)
    # That's why it'c called RDBMS (R for Relational)

    # This field "workshops" is related to the both models: Student model and Workshop model
    # so it can be placed inside either one of them
    # we placed it inside "Student" to make visible when we create/modify a student
    # it's many-to-many field
    # Refer to the code and the comment below for more understanding
    # This class field "ManyToManyField" requires a first argument 
    # which the name of the model it's related to as a string data type:
    # Then set blank=True to make NOT a required field 
    # because some student might not get the chance to take any workshop
    # But the company can give them the documents to read and unsderstand then to sign
    workshops = models.ManyToManyField('Workshop', blank=True)

    # We will override the __str__(self) method
    # To understand what this method is about, please check the comment for class Workshop
    
    # **********************************************************************************************
    # NOTE: 
    # Please notice that this function __str__(self) will become "useless" in the Admin page
    # after adding/modifying the "list_display" attribute in admin.py file or any template html page
    # We will keep this function for two reasons:
    # 1. for learning purpose, to review the basic solution before applying list_display
    # 2. it works when you run ORM commands using Python Shell. 
    #    Notice that if we comment this method and try to see the result with Python Shell
    #    We will receive this: <Student: Student object (1)>
    # **********************************************************************************************

    def __str__(self):
        # self is a python keyword => refers to the class "Student" itself
        # to access any field/attribute/property within the class itself (or outside the class):
        # self.field_name

        # You can use this way (similar to JS)
        # But notic that we used the function str() to cast/covnert the numeric data to be string
        # return self.first +" "+ self.last + " | Course: " + self.course + " | Average: " + str(self.average)
        # Or we can use the f string format:
        return (f"{self.first} {self.last} | Cousre: {self.course} | Average: {self.average}")

# ************************* Ending of Class Student *********************************


# making a model (Python class) for tracking the students 
# who took/finished any of Human right and Employment Law workshops
# These workshops give the student an idea about the main features of Ontario legislation governing: 
# Employment Contract Workshop
# Employment Standards Workshop
# Employment Rights Workshop
# Employment Equity Workshop

# creating a new class to track these workshops named "Workshop" 
# and it also inhirits from models.Model:
class Workshop(models.Model):
    # In this class we need to know just the name of each workshop that the student has finished:

    # **********************************************************************************************
    # Note: I had to add this attribute: default=""
    # Reason why, if we don't specify the default value, we recieve this error:
    # You are trying to add a non-nullable field 'workshop_name' to workshop without a default; we can't do that (the database needs something to populate existing rows).
    # Please select a fix:
    #  1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
    #  2) Quit, and let me add a default in models.py
    # *********************************************************************************************
    workshop_name = models.CharField(max_length=40, default="")

    # Notice that workshop_name is our python variable in this class
    # But Django will display it as"Workshop name" in the adminstrative page (admin)

    # We need to define the realtionship between these two models (Py Classes or DB Tables): 
    # Student class and Workshop class
    # A student can have many workshops 
    # A workshop can have many students
    # So this is a many-to-many relationship
    # We will use many-to-many relationship field

    # Where can we create or add this many-to-many rrelationship field?
    # NOTES about this field:
    ## - It's unique a field
    ## - Can be defined on either model (we can put it inside Student or inside Workshop)
    # We will put it in the student model
 
    # NOTE:
    # When you visit the admin page:
    # you will see the workshops are listed as:
    # Workshop object (4)
	# Workshop object (3)
	# Workshop object (2)
	# Workshop object (1)
    # But we need the admin to see these workshop with the normal english title!
    # Example:
    # Instead of displaying "Workshop object (4)"
    # it should be English label: "Employment Equity"

    # we will overrid this built-in method __str__(self) and passing the argument "self" 
    # since it's a method in Python class (always has to have self as argument)
    # This method will tell Django what the string representation should be for this model
    def __str__(self):
        # Just return the attribute that attached to this method 
        # instead of the default string "Workshop object 1"
        return self.workshop_name # telling Python to return the name field of the workshop

# For learning:
# and so on for any class (model) you want to add to your project:
class AnyClassName(models.Model):
    pass

# Dear my students:
# For more information about Fields, you can check Django documentations:
# https://docs.djangoproject.com/en/3.0/ref/models/fields/

