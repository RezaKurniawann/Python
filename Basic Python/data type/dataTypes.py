# Data Type

'''
Text       :	str
Numeric    :	int, float, complex
Sequence   :	list, tuple, range
Mapping    :	dict
Set        :	set, frozenset
Boolean    :	bool
Binary     :	bytes, bytearray, memoryview
None       :	None
'''

print("----------------------")
x = 5
print (x, type(x))
x = str("Hello World")
print (x, type(x))
x = int(20)
print (x, type(x))
x = float(20.5)
print (x, type(x))
x = complex(1j)
print (x, type(x))
x = list(("apple", "banana", "cherry"))
print (x, type(x))
x = tuple(("apple", "banana", "cherry"))
print (x, type(x))
x = range(6)
print (x, type(x))
x = dict(name="John", age=36)
print (x, type(x))
x = set(("apple", "banana", "cherry"))
print (x, type(x))
x = frozenset(("apple", "banana", "cherry"))
print (x, type(x))
x = bool(5)	
print (x, type(x))
x = bytes(5)
print (x, type(x))
x = bytearray(5)
print (x, type(x))
x = memoryview(bytes(5))
print (x, type(x), "\n")

#random number
import random
print ("RANDOM NUMBER")
print (random.randrange(1,10))
print("----------------------")


