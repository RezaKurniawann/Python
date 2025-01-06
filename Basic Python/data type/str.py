#String
print ("STRING")
print ("-----------------")
print ("Slicing")
b = "Hello, World"
print (b[2:5]) # output : llo
print (b[:5]) # output : hello
print (b[2:]) # output : llo, World
print (b[-5:-2], "\n") # output : Wor

print ("Modify")
print (b.upper()) # upper case
print (b.lower()) # lower case
a = " Hello, World "
print (a.strip()) # removing whitespace
print (b.replace("l", "j")) # replace i word with j 
print (b.split(","), "\n") # returns a list where the text between the specified separator becomes the list items

print ("Concatenation")
a = "Hello"
b = "World"
c = a + b 
print (c)
c = a + " " + b # add space between a and b
print (c, "\n")

print ("String Format")
age = 19
txt = "1. My name is Reza, I am ", age #wrong way, it will return (string (My name is ...) and int (19)
print (txt) 
txt = f"2. My name is Kurniawan, I am {age}" #right way
print (txt)
price = 55
txt = f"3. The price is {price} dollars"
print (txt)
txt = f"4. The price is {price:.2f} dollars" #adding modifier
print (txt)
txt = f"5. The price is {10 * 20} dollars" #can contain python code like math operation
print (txt, "\n")

print ("Escape Character")
txt = "My Name is \"Reza Kurniawan\", I am 19"
print (txt, "\n")


# Other escape characters:
# \'    = Single Quote
# \\    = Backslash
# \n    = New Line
# \r    = Carriage Return
# \t    = Tab
# \b    = Backspace
# \f    = Form Feed
# \ooo  = Octal value
# \xhh  = Hex value

print ("Other String Method")
# capitalize()
s = "hello world"
print(s.capitalize())  # Output: Hello world (Converts the first character to upper case)

# casefold()
s = "HELLO WORLD"
print(s.casefold())  # Output: hello world (Converts string into lower case)

# center()
s = "hello"
print(s.center(20))  # Output: '       hello        ' (Returns a centered string)

# count()
s = "hello world"
print(s.count('o'))  # Output: 2 (Returns the number of times a specified value occurs in a string)

# encode()
s = "hello world"
print(s.encode())  # Output: b'hello world' (Returns an encoded version of the string)

# endswith()
s = "hello world"
print(s.endswith('world'))  # Output: True (Returns true if the string ends with the specified value)

# expandtabs()
s = "hello\tworld"
print(s.expandtabs(8))  # Output: 'hello   world' (Sets the tab size of the string)

# find()
s = "hello world"
print(s.find('world'))  # Output: 6 (Searches the string for a specified value and returns the position of where it was found)

# format()
s = "Hello {}"
print(s.format('world'))  # Output: Hello world (Formats specified values in a string)

# format_map()
s = "Hello {name}"
print(s.format_map({'name': 'world'}))  # Output: Hello world (Formats specified values in a string)

# index()
s = "hello world"
print(s.index('world'))  # Output: 6 (Searches the string for a specified value and returns the position of where it was found)

# isalnum()
s = "hello123"
print(s.isalnum())  # Output: True (Returns True if all characters in the string are alphanumeric)

# isalpha()
s = "hello"
print(s.isalpha())  # Output: True (Returns True if all characters in the string are in the alphabet)

# isascii()
s = "hello"
print(s.isascii())  # Output: True (Returns True if all characters in the string are ascii characters)

# isdecimal()
s = "12345"
print(s.isdecimal())  # Output: True (Returns True if all characters in the string are digits)

# isdigit()
s = "12345"
print(s.isdigit())  # Output: True (Returns True if all characters in the string are digits)

# isidentifier()
s = "hello_world"
print(s.isidentifier())  # Output: True (Returns True if the string is an identifier)

# islower()
s = "hello"
print(s.islower())  # Output: True (Returns True if all characters in the string are lower case)

# isnumeric()
s = "12345"
print(s.isnumeric())  # Output: True (Returns True if all characters in the string are numeric)

# isprintable()
s = "hello"
print(s.isprintable())  # Output: True (Returns True if all characters in the string are printable)

# isspace()
s = "   "
print(s.isspace())  # Output: True (Returns True if all characters in the string are whitespaces)

# istitle()
s = "Hello World"
print(s.istitle())  # Output: True (Returns True if the string follows the rules of a title)

# isupper()
s = "HELLO"
print(s.isupper())  # Output: True (Returns True if all characters in the string are upper case)

# join()
s = "-"
print(s.join(['hello', 'world']))  # Output: hello-world (Joins the elements of an iterable to the end of the string)

# ljust()
s = "hello"
print(s.ljust(10))  # Output: 'hello     ' (Returns a left justified version of the string)

# lower()
s = "HELLO"
print(s.lower())  # Output: hello (Converts a string into lower case)

# lstrip()
s = "   hello"
print(s.lstrip())  # Output: 'hello' (Returns a left trim version of the string)

# maketrans() dan translate()
s = "hello world"
table = s.maketrans('h', 'j')
print(s.translate(table))  # Output: jello world (Returns a translation table to be used in translations)

# partition()
s = "hello world"
print(s.partition(' '))  # Output: ('hello', ' ', 'world') (Returns a tuple where the string is parted into three parts)

# replace()
s = "hello world"
print(s.replace('world', 'Python'))  # Output: hello Python (Returns a string where a specified value is replaced with a specified value)

# rfind()
s = "hello world world"
print(s.rfind('world'))  # Output: 12 (Searches the string for a specified value and returns the last position of where it was found)

# rindex()
s = "hello world world"
print(s.rindex('world'))  # Output: 12 (Searches the string for a specified value and returns the last position of where it was found)

# rjust()
s = "hello"
print(s.rjust(10))  # Output: '     hello' (Returns a right justified version of the string)

# rpartition()
s = "hello world"
print(s.rpartition(' '))  # Output: ('hello', ' ', 'world') (Returns a tuple where the string is parted into three parts)

# rsplit()
s = "hello world world"
print(s.rsplit(' '))  # Output: ['hello', 'world', 'world'] (Splits the string at the specified separator, and returns a list)

# rstrip()
s = "hello   "
print(s.rstrip())  # Output: 'hello' (Returns a right trim version of the string)

# split()
s = "hello world"
print(s.split(' '))  # Output: ['hello', 'world'] (Splits the string at the specified separator, and returns a list)

# splitlines()
s = "hello\nworld"
print(s.splitlines())  # Output: ['hello', 'world'] (Splits the string at line breaks and returns a list)

# startswith()
s = "hello world"
print(s.startswith('hello'))  # Output: True (Returns true if the string starts with the specified value)

# strip()
s = "   hello   "
print(s.strip())  # Output: 'hello' (Returns a trimmed version of the string)

# swapcase()
s = "Hello World"
print(s.swapcase())  # Output: hELLO wORLD (Swaps cases, lower case becomes upper case and vice versa)

# title()
s = "hello world"
print(s.title())  # Output: Hello World (Converts the first character of each word to upper case)

# translate()
s = "hello world"
table = str.maketrans('h', 'j')
print(s.translate(table))  # Output: jello world (Returns a translated string)

# upper()
s = "hello world"
print(s.upper())  # Output: HELLO WORLD (Converts a string into upper case)

# zfill()
s = "42"
print(s.zfill(5))  # Output: 00042 (Fills the string with a specified number of 0 values at the beginning)






