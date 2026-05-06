# Task 1

my_list = [4, 55, 66, 7787, 88, 89, 444];
max_number = my_list[0];

for item in my_list:
    if(max_number < item):
        max_number = item;

print(max_number)

max_number_1 = max(my_list);
print(max_number_1)

# Task 2

# Recursive functions
def fib(num):
    if(num == 0):
        return 0
    if(num == 1):
        return 1
    
    return fib(num - 1) + fib(num - 2);

print("fib(4) = ",fib(6));

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,

# Task 3
my_str = "a1b2c3d4e5f6g7h8i9"
reversed_str = ""

for char in my_str:
    reversed_str = char + reversed_str;

print(reversed_str[0:len(reversed_str):2])

my_str_1 ="123456789"
print(my_str_1[::-1][::2]) # Simple and more concise