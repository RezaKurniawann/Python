'''
All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

'''

class person:
    def __init__(self, name, age): 
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
    def personFunction(self):
        print ("Hello my name is", self.name, "And i'm", self.age, "years old" )

p1 = person ("Reza Kurniawan", 19)

print (p1.name)
print (p1.age)
print (p1)
print (p1.__dict__)
p1.personFunction()
p1.age = 20
print (p1.age)
del p1.age
# print (p1.age) - eror because p1.age no exist
del p1 # delete object 
        