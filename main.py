print("hello world")

# what is pipenv? what is a virtual environment?
# instance of dependencies for the program in question

# what does pipenv shell do?
# starts up the virt environment with your dependencies

# what is pip? how do we install new packages?
# downloads packages for your global environment (across your computer)

################# things that will be on the assessment: ################
# 1. I will be asking about virtual environment (pipenv)
# 2. possibility I'll ask about how to import
# 3. sql
# 4. procedural python
# 5. classes & instances
#########################################################################

# imports #
# import ipdb
import pytest # how to import packages

from my_file import do_stuff # how to import from other files
# modules - techinical term for the files we're pulling from

from somewhere.some_file import some_function # going into directories

def another_func():
    import ipdb # local to this fn
    ipdb.set_trace()

# ipdb.set_trace() # cannot access since it's outside the fn



# procedural python #

my_list = [1, 3, 4, 6, 8, 10]


for num in my_list: # for loops
    print(num)


for i in range( 0, len(my_list) ):
    # i = 3
    print( my_list[i] )


i = 0
while i < len( my_list ):
    print(my_list[i])
    i += 1

# list comprehension
squared_list = [ num**2 for num in my_list ]
evens = [ num for num in my_list if num % 2 == 0 ]

# for practice look at parrot lab or countdown to midnight lab


# classes and instances #

class Mammal:
    # mammal_list = []

    def __init__(self): # this init does not get used in the cat class
        print("WOW ITS A MAMMAL")
        # Mammal.mammal_list.append(self)

    def grow_fur(self): # this can be used normally in the cat class
        print("GROWING FUR SOUNDS")

    def show_off_personality(self):
        print("I AM A MAMMAL SHOWING OFF MY PERSONALITY")


class Cat(Mammal): # class

    favorite_herb = "catnip" # class attribute
    # Cat.favorite_herb --> "catnip"
    # ms_kitty.favorite_herb --> "catnip"

    favorite_postal_item = "box" # class attribute

    all_cats = [] # Cat.all_cats

    @classmethod # the decorator makes it a class method
    def some_class_method(cls):
        return "I am a class method"
    # Cat.some_class_method()
    # NOT ALLOWED TO DO Cat.purr() since it's an instance method
    # ms_kitty.some_class_method() but generally not for ms_kitty

    def some_instance_method(self):
        Cat.some_class_method()

    @classmethod
    def print_all_cats(cls):
        for cat in cls.all_cats:
            print(cat)

    def __init__(self, name, incoming_age_argument): # instance method
        self.name = name # just a normal attribute of Cat
        self.age = incoming_age_argument
        Cat.all_cats.append(self)
        # self is the particular instance

    def purr(self): # instance method --> ms_kitty.purr
        "PURRRRRRRRRRRRRRRRRRRRRRRRR"

    def show_off_personality(self):
        super().show_off_personality() # does both the cat version and mammal version
        print("I AM WEIRD AND QUIRKY")

    @property
    def age(self):
        print("GETTER IS BEING TRIGGERED")
        return self._age
    
    @age.setter
    def age(self, value):
        print("SETTER IS BEING TRIGGERED")
        if value >= 0:
            self._age = value
        else:
            raise TypeError("Age cannot be less than 0")


ms_kitty = Cat(name="Ms Kitty") # this is an instance

type(ms_kitty) # Cat
isinstance(ms_kitty, Cat) # True