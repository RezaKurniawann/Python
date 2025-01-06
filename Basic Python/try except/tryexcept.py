''''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''
print("\nException Handling")

try:
    print(x)
except:
    print("An exception occurred")

print("\nMany Exception")
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

print("\nElse")
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

print("\nFinally")
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

print("\nExample")
while (True):
    try:
        with open("data.txt", 'r') as file:
            print (file.read())
        break
    except :
        print ("file data.txt cannot find, make new file")
        with open ("data.txt", 'w', encoding='utf-8') as file:
            file.write("Hello my name is Reza Kurniawan")
        break

   

print("\nRaise an exception")
# Uncomment to raise an error and stop the program
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

x = "hello"
if not isinstance(x, int):
    raise TypeError("Only integers are allowed")
