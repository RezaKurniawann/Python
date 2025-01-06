# key function for working with the files in the python is the open () function
# open () function takes two parameters; filename, and mode

'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

'''
print ("=========== Read ============")
file = open ("data.txt", 'r')
print (file.read())
file.close()

print ()
file = open ("data.txt", 'r')
print (file.read(3)) # specify how many characters want to return
file.close()

print ()
file = open ("data.txt", 'r')
print (file.readline()) # can return one line by using the readline ()
print (file.readline())
file.close()

print ()
file = open ("data.txt", 'r')
for x in file:
    print (x)
file.close()

print ("=========== Write ============")
file = open ("data2.txt", 'a')
file.write ("data 2 write")

file = open ("data2.txt", 'r')
print (file.read())
file.close()

print ("=========== Delete ============")
#to delete a file, must import the OS module, and run its os.remove () 
import os
if os.path.exists ("data2.txt"):
    os.remove ("data2.txt")
    print ("File data 2 removed")
else :
    print ("File does not exist")


