# Python Programming 

## Environment setup (Comparing to NodeJS)

1. Install the Python latest version (3.14.4 during this session). Similar to NodeJS 
2. This will install the `pip`, a package manager for the python similar to `npm` for Node JS
3. Run the below command, this will install the Notebook interface for the Python development. This makes the pythong development easy.
```bash
pip install notebook
```
4. Post installing the notebook, we can run below command in terminal to launch the web based coding envionment  
```bash
jupyter notebook
```
5. If All goes good, we are good to run the app in there, if not we can open the `IDLE` in our local. This will open the python terminal. here also we can run the python programs
    - For running multi line code, 
    - we can create a `new file`
    - implement the code
    - post click the `run as module` 

## Concepts

### How to comment in python?

```python
'''
print("Multiline Commented out")
'''

print("Executes")
```

### How to print?

```py
count = 0
print("hello")
print(f"Sam is occuring {count} times") # Sam is occuring 0 times
```

### How to declare the variable?

- Unlike other Programming language we dont need a variable declaration keywords or data type to initialze the variable

```py
a = 10; # We should Declare and Initializ the variable at same time.
```

### Data types in Python

#### Basics: 
1. Integer - both -ve & +ve
2. Boolean - True / False
3. Float - All decimal numbers
4. Strings - both single & double quotes
6. Complex - number with real & imagenery parts 

#### Collections
1. List - Orderered and mutable - defined in `[]` - (duplicates are allowed)
2. Tuple - Ordered & immutable - defined in `()` - (duplicates are allowed)
3. Dictionery - Unordered & Unique keys and key - value pairs - defined in `{}`
4. Set - Unordered & Unique values - defeined as `{}` or `set()`

##### Type check

- To get the type of the variables we can use `type` function.

```py
a= 10;
print(type(a)); # <class 'int'>
```

### String Operations

```py
str_1 = "python";
str_2 = "Hello";

print(str_1 + str_2); # pythonhello - String Concatenation
print(5 * str_1); # pythonpythonpythonpythonpython 
print("Count of the string {str_1}",str_1[0]);
print("Count of the string {str_1}",str_1[1]);
print("Count of the string {str_1}",str_1[2]);

# String slicing
# Syntax [(Integer type)Start Index : (Integer type)End Index (not inclusive) : (Integer type) Step]
# (Step): The "stride" or increment. Instead of taking every character, it takes every n charactes
# returns the string
print('String was sliced from index 0 to 1', str_1[0: 2]); # py, the 2nd index is not included.
```

#### Step - Slicing

```py
str = "Accenture";
print(str[0: 9: 3]) # Aeu, here the A, E, U are the characters that are present in every 3rd step
```

```py
str = "hello";
len(str); # 5 returns the lenth of the string
str.count("") # accepts the correspoding character and returns the number of occurance that character was repeated
```

#### Split and Strip

### List Operations

#### Add 

#### Remove