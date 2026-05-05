# Task 1
# Using 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
# Sample input 
# Sample output 
#  SaKellymy

# Task 1
s1 = "Samy"
s2 = "Kelly"

print(s1[0:3] + s2 + s1[2: 4]);

print(len(s1));

# task 2
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

# task 3
str2 = "English = 78 Science = 83 Math = 68 History = 65"
# str2 = input("Enter the subject and marks")
numberCount = 0;
avg = 0;
sum = 0

for char in str2.split():
    if(char.isdigit()):
        numberCount += 1;
        sum += int(char);

print("Sum", sum);
print("Avg", sum / numberCount);

# task 4
str3 = "My name is Sam I live in Mumbai"

splitedStr = str3.split()
idx = len(splitedStr) - 1;
str4 = ""

while(idx >= 0):
    str4 += splitedStr[idx] + " ";
    idx -= 1;

print(str4.strip())

# task 5
str5 = "My name is Sam.  Sam lives in Mumbai. Sam plays cricket."
count = str5.lower().count('sam')

print(f"Sam is occuring {count} times");

# task 6
myList = [10, 20, 30, 20, 50, 100];

firstOccuarnaceIdx = myList.index(20);

myList[firstOccuarnaceIdx] = 200;

print(myList);

# task 7 (Sort)
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d',29)); # (('c', 11), ('a', 23), ('d', 29), ('b', 37))

convertedList = list(tuple1)

print(convertedList)