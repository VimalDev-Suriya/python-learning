# Required Arguments
# def myFunction(param1, param2):
#     print(param1, param2);

# myFunction(); # this will throw error - since by default python will consider as the required param

# Default ARguments
def myFunction(param1, param2="coming from default"):
    print("Params Example - Default => ", param1, param2);

myFunction("param 1");

# Keyword Arguments
def myFunction(param1="Default - 1", param2="Default - 2"):
    print("Params Example - Keyword => ", param1, param2);

myFunction(param2="hello");

# Variable length
def myFunction(*x):
    print('Params Example - Variable length => ', x);
    print(type(x)); # Tuple

myFunction(1, 2, 3, 4, 5)
myFunction(True, 1.3, "hello", (1, 2, 3), [1, 2, 3], {1, 2}, {"a": 1})

# Different type of passing the Dictionery - Dictionaries are passed by reference

# Single dictionery
def process_user_1(user_dict):
    # Access keys using standard indexing
    print(f"Name: {user_dict['name']}")
    print(f"Age: {user_dict['age']}")

data = {"name": "Alice", "age": 30}
process_user_1(data)

# Destructing the object
# The Functions param should exactly match the keys of the Dictionery
def process_user_2(name, age):
    # Access keys using standard indexing
    print(f"{name} is {age} years old.")
    

data = {"name": "Alice", "age": 30}
process_user_2(**data); # Destructing in JS or Unpacking in Python [double splat operator **]

# Passing lot of properties without kowing the keys
def process_user_3(**kwargs):
    print(type(kwargs))# <class 'dict'>
    for key, value in kwargs.items():
        print(f"key = {key} & value = {value}")

data = {"name": "Alice", "age": 30}
process_user_3(**data); # Destructing in JS or Unpacking in Python