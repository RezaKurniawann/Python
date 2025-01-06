#Creating function
def my_function () :
    print ("Hello from a function")

#Calling a function
my_function ()

print ("\nArguments")
def my_function (name) :
    print ("Hello,", name)

my_function("Reza")

def my_function (fname, lname ) :
    print ("Hello,", fname, lname)

my_function ("Reza", "Kurniawan")

# arbitrary arguments *args, if dont know how many arguments that will be passes itu function can use * 
def my_function (*kids) : 
    print ("The youngest child is " + kids [2])

my_function ("Emil", "Tobias", "Linus")

#keyword arguments
def my_function (child3, child2, child1) : 
    print ("The youngest child is " + child3)

my_function (child1 = "Reza", child2 = "Kurniawan", child3 = "Awan")

#Arbitrary keyword arguments **kwargs, if dont know how many keyword arguments that will be pass into function can use **
def my_function (**kid):
    print ("His last name is  " + kid["lname"])

my_function (fname = "Reza", lname = "Kurniawan")

print ("\n Default Parameter value")
def my_function (country = "Norway") :
    print ("I am from " + country)
my_function ()
my_function ("Indonesia")

print ("\nPassing a List as an Argument")
def my_function (food) :
    for x in food :
        print (x)

fruits = ["apple", "banana", "cherry"]
my_function (fruits)

print ("\nReturn Values")
def my_function (x):
    return 5*x 

print (my_function(3))
print (my_function(5))

print ("\nPositional-only Arguments")
def my_function (x, /) :
    print (x)
my_function(3)
'''
def my_function(x, /):
  print(x)

my_function(x = 3) #eror
'''


print ("Keyword-only Arguments")
def my_function (*, x):
    print (x)

my_function (x = 3)
'''
def my_function(*, x):
  print(x)

my_function(3) #eror
'''

print ("\nCombine Positional-only and Keyword-only")
def my_function (a, b, /, *, c, d):
    print (a, b, c, d)
    print (a + b + c + d)

my_function (5, 6, c = 7, d = 8)

print ("\nRecurtion")
def tri_recurtion (k) :
    if (k > 0):
        result = k + tri_recurtion (k-1)
        print (result)
    else:
        result = 0
    return result
    
tri_recurtion (6)



