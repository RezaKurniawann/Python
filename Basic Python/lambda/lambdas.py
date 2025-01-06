# a lambad function is a small anonymous function, lambda can take any number of arguments but can only have one expression
# lambda arguments : expression
x = lambda a : a + 10
print ("1.",x(5))

x = lambda a, b : a * b
print ("2.",x (5, 6))

x = lambda a, b, c : a + b + c
print ("3.", x (5, 6, 2))

def myFunction (n):
    return lambda a : a * n

myDoubler = myFunction(2)
myTripler = myFunction(3)
print ("4.",myDoubler(11))
print ("5.",myTripler(11))

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def myFunction (num) :
    return num < 5

x = list (filter(myFunction, numList))
print ("6.",x)
x = list (filter (lambda num : num < 7, numList))
print ("7.",x)
x= list (filter (lambda num : num%2 == 0, numList ))
print ("8.", x)



