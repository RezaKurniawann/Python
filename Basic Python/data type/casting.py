print("----------------------")
print("NUMBER")
x = 3 + 5j
y = 5j
z = -5j
print(x, type(x))
print(y, type(y))
print(z, type(z), "\n")

print("----------------------")
#Casting
print("CASTING")
w = "8"
x = 1 
y = 2.8
z = 1j

a = float (x)
b = int (y)
c = complex(x) 
d = float (w)

print (a, type(a)) #int to float
print (b, type(b)) # float to int
print (c, type(c))  #int to complex
print (d, type (d)) #string to float