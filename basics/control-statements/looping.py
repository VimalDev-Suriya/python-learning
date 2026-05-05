print("*********** While looping Statements ***********")
val = int(input('Enter the input value'));

while(val <= 10):
    print(val);
    val += 1;
else:
    print('Out of Loop')
print("*********** For looping Statements ***********")
myStr_2 = "Python";
myList_2 = [1, 2, 3, 4];
myTuple_2 = ("a", "b", "c");
myDictonery_3 = {
    "id" : "1",
    "Name": "SK"
}
mySet_3 = {1, 2, 3, 4, 5}

print('Looping String')
for i in myStr_2:
    print(i);

print('Looping list')
for i in myList_2:
    print(i);

print('Looping Tuple')
for i in myTuple_2:
    print(i);

print('Looping Dictionery')
for i in myDictonery_3:
    print(i); # Displays only keys
for i in myDictonery_3:
    print(myDictonery_3[i]); # Displays values

print('Looping Sets')
for i in mySet_3:
    print(i);

print('Looping from the Range')
# Syntax of range
# range(start, end(not inclusive), step)
for i in range(0, 10, 2):
    print("i", i)
print("*********** looping Statements ***********")