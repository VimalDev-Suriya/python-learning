# Functions

```py
# Function declaration
def functionaName(arg):
    return arg

functionName(param); # Function execution
```
In Python Functions cannot be hoisted, the below code snippet will throw error, as myFunction was not defined

```py
myFunction(1);

def myFunction(param:str):
    print(f"Function got executed with {param}")
```

Function overloading is not directly supported in python - but it is achievable. The below code snippet will throw error, like below. Python will actually override the function last recent function declaration

```py
def myFunction(param):
    print(f"Function got executed with {param}")

def myFunction(param1, param2):
    print(f"Function got executed with {param1} {param2}")

myFunction(1);
```
```
TypeError: myFunction() missing 1 required positional argument: 'param2'
```
- Python supports `return` as it can return the data.
- Unlike in JS, we can return the function as the param. But the closure concept is not capable in python

```py
def add(param1, param2):
    return param1 + param2;

result = add(1, 2);
print("Function ref",add); # this will log the function reference <function add at 0x778191c0e2a0>
print('result', result) # 3
```

```py
def add(param1, param2 = 1):
    def some():
        print('Hello');
    return some

result = add(1, 2);
result();
```

## Arguments

1. Required Params
```py
def myFunction(param1, param2):
    print(param1, param2);

myFunction(); # this will throw error - since by default python will consider as the required param
```
2. Default Params []
```py
def myFunction(param1, param2="coming from default"):
    print("Params Example - Default", param1, param2);

myFunction("param 1");
```
3. Keyword Params
4. Variable length param (*) & Dictionery type of param(**)