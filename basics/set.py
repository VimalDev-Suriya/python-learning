print("*********** Set ***********")
# Set
# Will not accept the duplicate values
# Always accept the Immutable values alone - List/Dictioneries are not acceted by it
# We cannot able to index - Non-subscriptable 

# Initializaing the Set
mySet = {267, True, "String", (101, 102), "String"}

print(mySet); # {(101, 102), 1, 'String'}
mySet.add('Test');
print(mySet);

mySet_1 = {1, 2, 3, 4, 5, 6, 7};
mySet_2 = {4, 5, 6, 7, 8, 9, 10};

print("Union of 2 Set", mySet_1.union(mySet_2))
print("Union of 2 Set", mySet_1.union(mySet_2))

print("Intersection of 2 Set", mySet_1 & mySet_2);
print("Intersection of 2 Set", mySet_1.intersection(mySet_2))

print("Only Set A Items", mySet_1 - mySet_2);
print("Only Set B Items", mySet_2 - mySet_1);


print("All Unique values present between 2 sets",mySet_1 ^ mySet_2)
print("*********** Set ***********")