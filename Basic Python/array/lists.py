# List are used to store multiple items in a single variable
def fruitFunction():
    fruitList = ["apple", "banana", "cherry"]
    return fruitList

print("List")
fruitList = fruitFunction()
print("1.", fruitList)

# Allow duplicates
fruitList = ["apple", "banana", "cherry", "apple", "cherry"]
print("2.", fruitList)

# List dgth
print("3.", len(fruitList)) 

# Check data type
print("4.", type(fruitList)) 

# List can contain different data types
fruitList = ["abc", 34, True, 40, "male"]
print("5.", fruitList)

# list() constructor
fruitList = list(("Apple", "Banana", "Cherry"))  # note the double round brackets
print("6.", fruitList)

print("\nAccess Items")
carList = ["Lamborghini", "Ferrari", "Tesla"]
print("1.", carList[1])  # output: Ferrari 
print("2.", carList[-1])  # output: Tesla
print("3.", carList[0])  # output: Lamborghini
print("4.", carList[-2])  # output: Ferrari 

print("\nRange of index")
fruitList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("1.", fruitList[2:5]) 
print("2.", fruitList[:4]) 
print("3.", fruitList[2:]) 
print("4.", fruitList[-4:-1]) 

print("\nCheck if items exist")
if "apple" in fruitList:
    print("Yes, 'apple' is in the fruits list")
else:
    print("No, 'apple' is not in the fruits list")

print("\nChange Value")
fruitList = fruitFunction()
fruitList[1] = "blackcurrant"
print("1.", fruitList)

fruitList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruitList[1:3] = ["blackcurrant", "watermelon"]
print("2.", fruitList)

fruitList = fruitFunction()
fruitList[1:2] = ["blackcurrant", "watermelon"]
print("3.", fruitList)

fruitList[1:3] = ["watermelon"]
print("4.", fruitList)

print("\nInsert Items")
fruitList = fruitFunction()
fruitList.insert(2, "watermelon")
print("1.", fruitList)

# Append items (add an item to the end of the list)
fruitList.append("orange")
print("2.", fruitList)

print("\nExtend List")
fruitList = fruitFunction()
tropical = ["mango", "pineapple", "papaya"]
fruitList.extend(tropical)
print("1.", fruitList)

fruitList = fruitFunction()
fruitTuple = ("kiwi", "orange")
fruitList.extend(fruitTuple)
print("2.", fruitList)

print("\nRemove Items")
fruitList = fruitFunction()
fruitList.remove("banana")
print("1.", fruitList)

# If there is more than one item with the specified value, the remove() method removes the first occurrence
fruitList = ["apple", "banana", "cherry", "banana", "kiwi"]
fruitList.remove("banana")
print("2.", fruitList) 

# Remove specified index
fruitList = fruitFunction()
fruitList.pop(1)
print("3.", fruitList)

# Remove the last item if no index is specified
fruitList = fruitFunction()
fruitList.pop()
print("4.", fruitList)

# del can remove the specified index or delete the list completely
fruitList = fruitFunction()
del fruitList[0]
print("5.", fruitList)

fruitList = fruitFunction()
del fruitList

# Clear method empties the list, the list still remains but has no content
fruitList = fruitFunction()
fruitList.clear()
print("6.", fruitList)

print("\nLoop List")
# loop for
print("Loop for")
fruitList = fruitFunction()
for fruit in fruitList:
    print(fruit)
print()
fruitList = fruitFunction()
for i in range(len(fruitList)):
  print(fruitList[i])

#loop while
print()
print("Loop While")
fruitList = fruitFunction()
i = 0
while i < len(fruitList):
  print(fruitList[i])
  i = i + 1

#loop list comprehension
print()
print("Loop List Comprehension")
fruitList = fruitFunction()
[print(x) for x in fruitList]

