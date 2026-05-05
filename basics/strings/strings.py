# ********** String Operations ****************
print("********** String Operations ****************")
str_1 = "python";
str_2 = "Hello"

print("count",len(str_1))
print("How many times l repeats", str_2.count("l"))

print(str_1 + str_2); # pythonhello - String Concatenation
print(5 * str_1); # pythonpythonpythonpythonpython 
print("Count of the string {str_1}",str_1[0]);
print("Count of the string {str_1}",str_1[1]);
print("Count of the string {str_1}",str_1[2]);

# String slicing
# Syntax [start Index : End Index (not inclusive)]
print('String was sliced from index 0 to 1', str_1[0: 2]); # py, the 2nd index is not included.
print('String was sliced from index 0 to 1', str_1[0: 6: 5].upper()); # PN

# TASK
str = "Accenture";

print(str[0:3]); # Acc
print(str[1: 5]); # ccen
print(str[0: 8: 3]) # Aeu, here the A, E, U are the characters that are present in every 3rd step

# Strip and Split

sentence = "This is Python Programming";
sentence_1 = "This@is Python Programming@"

# Similar to JS split - 
# Splits the string and returns the array of strings.
# We can pass the "string / character" into the split functions
print(sentence.split()); # ['This', 'is', 'Python', 'Programming']
print(sentence_1.split("@")); # ['This', 'is Python Programming', '']
print('replcaed the empty speaces', sentence.replace(" ", ""))

# A built-in string method used to remove leading and trailing characters from a string
# Similar to trim() in JS
# returns the new modified string
# Accepts the character, which will always remove from First and last of the character
sentence_2 = "   Hello Python    "
sentence_3 = "@   Hello Python    @"
print(sentence_2.strip()); # "Hello Python"
print(sentence_3.strip("@")) # "   Hello Python    "

# A Function which helps to determin the existence of the particular character or element in the string/list
# Returns the Index if found if not -1 
print(sentence_1.find('@')); # retuns the first possible value 
print("********** String Operations ****************")

str1 = "P@#yn26at^&i5ve"
chars = 0;
digits = 0;
symbols = 0

for char in str1:
    if(char.isalpha()):
        chars += 1
    elif (char.isdigit()):
        digits+=1
    else:
        symbols+=1

print('Chars', chars)
print('Digits', digits)
print('Symbols', symbols)

# ********** String Operations ****************