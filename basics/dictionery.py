# *********** Dictonery ***********
print("*********** Dictonery ***********")

# Initializing the Dictionery ~= Object in arrays
# Dictoner are immutables
# Keys are always Immutable and always accept immutable type of Data like - String, Number, Boolean, Tuple
# Values are always mutable - we can always use the 
myDictonery = {
    "id" : 1,
    "Name": "SK",
    (101, 102): [1, 2, 3],
    1.1: "Number",
    True: "Boolean"
}

print(myDictonery["id"])
print(myDictonery["Name"])
print(myDictonery[(101, 102)])
print(myDictonery[1.1])
print(myDictonery[True])

# In Python, Duplicate Keys are accepted, but the values will be overrided by the last duplicate key
myDictonery_2 = {
    "id": "hello",
    "id": 1
}

print(myDictonery_2); # {"id": 1}

# Below code throws error 
# TypeError: unhashable type: 'list'
# myDictonery_1 = {
#     [1,2]: "test",
#     {1}: "hello"
# }

# print(myDictonery_1);

myDictonery["Add"] = "I was added";
print(myDictonery);

del(myDictonery["Add"]);
print(myDictonery)
print("*********** Dictonery ***********")