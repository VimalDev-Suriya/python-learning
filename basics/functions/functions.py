def myFunction(param):
    print(f"Function got executed with {param}")

myFunction(1);

# ******************************************************************

def add(param1, param2):
    return param1 + param2;

result = add(1, 2);
print("Function ref",add); # this will log the function reference <function add at 0x778191c0e2a0>
print('result', result) # 3

# *****************************************************************
def test():
    def some():
        print('Hello');
    return some

result = test();
result(); # hello