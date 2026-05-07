# Scenario 1: (Works fine)
name = "Name at top level Scope"

def some_function():
  print(name) # I can get "Name at top level Scope"

some_function()
print(name) # I can get "Name at top level Scope"


# Scenario 2: (This will return the error, as the function call is happened before initializing the variable name)

# def some_function_1():
#   print(name);

# some_function_1()
# name = "Hello!"

#*******************************************************************************
# Scenario 3: (Works fine)

def some_function_1():
  print(name_1);

name_1 = "Hello!"
some_function_1()

#*******************************************************************************
# Scenario 4: (Works fine)

def some_function_2():
  name_2 = "Some Another Hello!"
  print(name_2); # "Some Another Hello!"

name_2 = "Hello!"
some_function_2()
print(name_2); # "Hello!"

# In Python, all variables are scoped and whenever python encounters "=" or the non-pythonic variable, it will consider as the new variable, though the name of the variables are identical. 
# So the output will be like
# "Some Another Hello!" -> Inside the function 
# "Hello!" -> Outside the functiom

#*******************************************************************************
# Scenario 5 (Throws the error)

# def some_function_3():
#   print(name_3) # Here we get error, as discussed, here the "name_3" is a new variable and we cannot leave the un-initialized variable. So we will get unbound local variable.
#   name_1 = "Some Another Hello!"
#   print(name_3); # "Some Another Hello!"

# name_3 = "Hello!"
# some_function_3()
# print(name_3); # "Hello!"

#*******************************************************************************
# Scenario 6 (Works fine) - What we should do if we want to make the above code to work and share the comman variable which was declared at top level

def some_function_4():
  global name; # This tells the compiler that this is not the local one, it is the one deckared at toplevel.
  print(name);
  name = "Someother Hello"
  print(name)

name = "Hello !"
some_function()
print(name)

# "Hello"
# "Someother Hello"
# "Someother hello"
#*******************************************************************************

# Scenario 7

def outer():
  local_outer = "X";

  def inner():
    local_outer = "Y";
    print(local_outer); # "Y"
    
  print(local_outer); # X
  return inner();

# out = outer();
# out();
outer()(); # This syntax is also supported in python
#*******************************************************************************

# Scenario 8

def outer():
  local_outer = "X";

  def inner():
    nonlocal local_outer; # After providing "nonlocal" we can access the variables from lexical scope not the global
    local_outer = "Y";
    print(local_outer); # "Y"
    
  print(local_outer); # Y
  return inner();

out = outer();
out();

