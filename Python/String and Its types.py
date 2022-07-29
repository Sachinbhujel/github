# Strings:- Text is string datatypes.
# Any data type written as text is a string.
# Any data under single, double or triple quote are strings.

name = "Sachin Bhujel"
print(name)
print(name[0])  # print 0th index value

# Multiline string:- 
multiline_string = '''I am a Sachin Bhujel
I like to play bgmi'''
print(multiline_string)

# Escape Squence in strings
print("I am fire\nAnd how are you?") # line break (\n: new line)
print("Days\tTopics\tExeecises") # adding tab space or 4 spaces(\t)
print("This is a backslash symbol \\") # To write a backslash
print('Hello world\'s') # To write a single quote inside a single quote
print("Hello world\"s") # To write a double quotes inside a double quotes.

# upper
print(name.upper())

# lower
print(name.lower())

# length 
print(len(name))

# find
print(name.find("H"))

# replace
print(name.replace("S", "P"))

# exist
print("sachin" in name)




