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
print(my_str_1[::-2]) # Simple and more concise - as the step field can go from the last and log only alternate values

# Task 4
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def fib_2_numbers(a, b):
    my_list = [int(a), int(b)]
    
    while True:
        # temp = my_list[len(my_list) - 2] + my_list[len(my_list) - 1];
        temp = my_list[-2] + my_list[-1]; # Array's last element can be accessed by passing the -ve numbers as index
        if(temp > 1000):
            break
        my_list.append(temp);
    
    print(my_list) # [100, 2, 102, 104, 206, 310, 516, 826]
    # for num in my_list:
    #     if(temp > 1000):
    #         break;
        
    #     temp = my_list[len(my_list) - 2] + my_list[len(my_list) - 1];
    #     my_list.append(temp);

    # print(my_list) # [100, 2, 102, 104, 206, 310, 516, 826, 1342]
        
fib_2_numbers(100, 2)
