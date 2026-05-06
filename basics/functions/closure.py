# Below code will fail, because unlike in JS, which have scope chain to find the value of the variables from child to its parents. But in python it is LEGB rule (Local, Enclosing, Global, Built-in) for looking up variables.

# By default we can only "read" the variable from parent. If we need to make sure that the corresponding variable need to be updated in future. then we need to handle add few properies

'''
def counter_instance(initialCount):
    count = initialCount;

    def counter():
        count += 1; # here the count is the NEW Variable, which will be created within the counter function scope. Python will try to add 1 to it, since count is the new variable it wont have any values in it. so here it is the syntax error
        print(count);

    return counter;

counter_1 = counter_instance(1);
counter_1(); 
'''

def counter_instance(startWith):
    count = startWith;

    def counter(step=1):
        nonlocal count; # This is the magic bridge to the parent scope. (which help compiler to visit the parent first and then go to global)
        count += step;
        print(count);

    return counter;

counter_1 = counter_instance(0);
counter_1(1); 
counter_1(4); 

counter_2 = counter_instance(0);
counter_2();
counter_2();
