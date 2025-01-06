def fruitFunction () :
    fruitTuple = ("apple", "banana", "cherry")
    return fruitTuple

fruitTuple = fruitFunction ()
print (fruitTuple)
print("1. Fruit length =",len(fruitTuple))
fruitTuple = ("apple",)
print("2.",type(fruitTuple)) #tupple
fruitTuple = ("apple")
print("3.",type(fruitTuple)) #string

# tuple can contain different data types
tuple1 = ("reza", 19, True, 2004, "male")
print("4.", tuple1)

# tuple constructor
fruitTuple = tuple (("apple", "banana", "cherry")) # note the double roundbrackets
print ("5.", fruitTuple)


#Acces Tuple items
print ("\nAcces items")
fruitTuple = fruitFunction ()
print ("1.", fruitTuple[1]) #banana
print ("2.", fruitTuple[-1]) #cherry

print ("\nRange of Indexes")
fruitTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print ("1.", fruitTuple[2:5])
print ("2.", fruitTuple[:4])
print ("3.", fruitTuple[2:])
print ("4.", fruitTuple[-4:-1])

print("\nCheck if items exist")
fruitTuple = fruitFunction ()
if "apple" in fruitTuple:
    print("Yes, 'apple' is in the fruits tuple")
else :
    print("No, 'apple' is in the fruits tuple")

print("\nChange Value")
#once a tuple is created, cannot change its value so need convert to the list 
fruitList = list (fruitTuple)
fruitList [1] = "kiwi"
fruitTuple = tuple (fruitList)
print ("1.",fruitTuple) 

print("\nAdd items")
fruitTuple = fruitFunction ()
fruitList = list (fruitTuple)
fruitList.append("orange")
fruitTuple = tuple (fruitList)
print ("1.", fruitTuple)

# add tuple to a tupple
newFruitTuple = ("watermellon", )
fruitTuple += newFruitTuple
print ("2.", fruitTuple)

print("\nRemove items")
fruitList = list (fruitTuple)
fruitList.remove("apple")
fruitTuple = tuple (fruitList)
print ("1.", fruitTuple)

# delete tuple completely
fruitTuple = fruitFunction ()
del fruitTuple

print ("\nUnpacking a Tuple")
fruitTuple = fruitFunction ()
(green, yellow, red) = fruitTuple
print ("1.",green)
print ("2.",yellow)
print ("3.",red)

# if the number of variabless is less than ne number of values, can add an * to the variable name
fruitTuple = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruitTuple
print("4.",green)
print("5.",yellow)
print("6.",red)

fruitTuple = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *tropic, red) = fruitTuple
print("7.",green)
print("8.",tropic)
print("9.",red)

print("\nLoop Tuples")
fruitTuple = fruitFunction ()
print ("For Loop")
for i in range (len (fruitTuple)):
    print (fruitTuple[i])
print ("While Loop")

while i < (len (fruitTuple)):
    print (fruitTuple[i])
    i = i + 1

print("\nJoin Tuples")
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print ("1.",tuple3)
#multiply tuple
tuple4 = tuple1 * 2
print ("2.", tuple4)

print ("\nTuple Method")
#count
my_tuple = (1, 2, 3, 2, 4, 2, 5)
countTuple = my_tuple.count(2)
print(f"Number of occurrences of the number 2: {countTuple}")
#index
indexTuple = my_tuple.index(2)
print(f"The first index value of 2 was found: {indexTuple}")








