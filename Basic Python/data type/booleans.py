a = 200
b = 33

if b > a:
    print ("B is greater than a")
else :
    print ("B is not greater than a")

x = "Hello"
y = 15

print (bool(x)) #non-empty string. In Python, any non-empty string is considered True.
print (bool(y)) #non-zero number. In Python, any non-zero number is considered True.

# output : true
exampleStr = bool ("abc")
exampleInt = bool (123)
exampleList = bool(["apple", "cherry", "banana"])
print (exampleStr, exampleInt, exampleList)

# output : false
a = bool(False)
b = bool(None)
c = bool(0)
d = bool("")
e = bool(())
f = bool([])
g = bool({})

print (a, b, c, d, e, f, g)

def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int))