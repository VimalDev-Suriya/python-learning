'''
def instance_fn(cb):
    def wrapper_fn():
        print("*" * 10)
        cb();
        print("*" * 10)
    return wrapper_fn;

def hello():
    print('Hello Python')

# without decorator we need to create a instance and we need to execute the code.
hello_instance = instance_fn(hello);
hello_instance(); 
'''

# with decortor
def instance_fn(cb):
    def wrapper_fn():
        print("*" * 10)
        cb();
        print("*" * 10)
    return wrapper_fn;

# Below is the decorator
@instance_fn
def hello():
    print('Hello Python')

# Below lines are 
# hello_instance = instance_fn(hello);
# hello_instance(); 

# Due to decorator, we dont want to create a cb function from instance_fn. The python compiler can do this by default if it encounters the decorators
hello();

# ***************************************************************************************

# We can create multiple decorators
# with decortor
def instance_fn(cb):
    def wrapper_fn():
        print("*" * 10)
        cb();
        print("*" * 10)
    return wrapper_fn;

def instance_fn_1(cb):
    def wrapper_fn():
        print("@" * 10)
        cb();
        print("@" * 10)
    return wrapper_fn;

# Below is the Multiple decorators
# @instance_fn_1 will execute first
# instance_fn will exeute next
@instance_fn_1
@instance_fn
def hello():
    print('Hello Python')

hello()
'''
Output will be like below
@@@@@@@@@@
**********
Hello Python
**********
@@@@@@@@@@
'''