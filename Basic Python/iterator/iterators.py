'''
iterator is an object that contains a countable number of values

in python, iteraotr is an object which implements the iterator protocol,
which consist of the methods __iter__() and __next__
'''

print ("Iterator vs iterable")
#list, tuple, dictionarie, and set are all iterable object
myTuple = ("apple", "banana", "cherry")
myit = iter (myTuple)

print (next(myit))
print (next(myit))
print (next(myit))

myStr = "banana"
myit = iter (myStr)
print (next(myit))
print (next(myit))
print (next(myit))
print (next(myit))
print (next(myit))
print (next(myit))

