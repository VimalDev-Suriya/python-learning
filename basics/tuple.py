# ************** Tuple ******************
# I cannot mutate the values present in Tuple
print("*********** Tuple ***********")
my_tuple = ("hello", 1, 2);
print(my_tuple);
print(type(my_tuple));

my_tuple_1 = ("hello");
print(type(my_tuple_1)); # string - As the tuple
print(my_tuple_1); # Hello
print("*********** Tuple ***********")

# Now we can think - why can't we use a single tuple to create a constant variables in python?
# Answer is NO. Before explaining about the reason we should understand the diff between Immutable and Constant Object. 

# Immutable means - we cannot change the value of the corresponding variables, like we cannot add new item into tuple object
# Contant means - we cannot able to re-assign the new value to the variable itself.

# in Python 
my_typle = "hello"; 
print(my_tuple); # Hellow - this is 100% valid.
