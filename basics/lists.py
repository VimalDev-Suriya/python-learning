# *************** List *****************
print("************** List *****************")
# Initializing the Array/List
# [] represents the list and it is mutable
myList = ["hello", True, 1.2];

print(myList[1]);
# help(type(myList)); # for determining the methods and functions present under the particular object

# Append - Similar to JS push
# Add the value at the last of the list
# Returns "None" data type
print("Append",myList.append([1, 2, 3])); # ['hello', True, 1.2, [1, 2, 3]]
print(myList);

# Extend - similar to JS concat
# Returns "None" data type
print("Extend",myList.extend([1, 2, 3])); # ['hello', True, 1.2, 1, 2, 3]
print(myList)

# Insert
# Adding the value to the specific index
# Syntax - insert(index, element)
# Returns "None" data type
print("Insert ",myList.insert(0, "Inserted First"));
print(myList)

# remove the first occuarnace of the value;
# Accepts the Value
# Return "None" type
# Throws error if the element is not found
print(myList.remove("Inserted First"));  
print(myList);

# remove the first occuarnace of the index;
# Accepts the Index
# Return the value which was removed
print(myList.pop(0))
print(myList)

# del - is the global function to delete the elements
del(myList[1: 3]);
del(myList[1]);
print("Del",myList)

# Cleans the entire array and 
print(myList.clear());
print("MyList after clean",myList); # []
print("************** List *****************");
# *************** List *****************
