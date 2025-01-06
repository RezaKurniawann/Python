print ("Local Scope")
def myFunction ():
    x = 300
    print (x)
myFunction ()

def myFunction ():
    x = 300
    def myInnerFunction ():
        print (x)
    myInnerFunction ()
myFunction()

print ("\nGlobal Scope")
x = 300
def myFunction () :
    print (x)
myFunction ()
print (x)

print ("\nNaming Variables")
#function will print the local x and then the code will print the global x
x = 300

def myFunction () :
    x = 200
    print (x)
myFunction ()
print (x)

print ("\nGlobal Keyword")
def myFunction ():
    global x #makes the variable global
    x = 300
myFunction ()
print (x) 

x = 300
def myFunction ():
    global x 
    x = 200
myFunction () # to change the value of global variable with variable inside function
print (x) #200

print ("\nNonlocal Keyword")
def myFunction1 ():
    x = "Reza"
    def myFunction2 ():
        nonlocal x
        x = "hello"
    myFunction2() # nonlocal keyword makes the variable belong to the outer function.
    return x
print (myFunction1())


