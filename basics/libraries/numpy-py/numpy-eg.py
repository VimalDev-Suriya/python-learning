# This is how we can import the library
# "as" represented as the alias
import numpy as np;

v1 = np.array([1, 2, 3, 4, 5]);
print(v1, type(v1))

v2 = np.array([[1,2], [3, 4], [5, 6]])
print("V2 Matix ",v2);
print("Number of rows and columns in the V2 matrix is = ", v2.shape) # shape is the propery that help to determine the rows * column
print("Total number of items = ", v2.size) # 2 * 3
print('Data type of the elements stored in V2 ', v2.dtype) # int

# Below code will throw error - because there are not homogenous in shape
# v3 = np.array([[1,2,10], [3, 4], [5, 6]])
# print('V3 Matrix', v3)

# from the size of matrix from 2 * 3 to 3 * 2
reshaped_v2 = v2.reshape(3, 2)
print("Re-shaping the structure of Matix", reshaped_v2);

# Creating the 2D Matrix with the given size filled with 0's
v3 = np.zeros([3,3])
print('V3 with Zeros float', v3)
'''
[
    [0., 0.],
    [0., 0.],
    [0., 0.]
]
'''

# Based on the second argument, the value of the array will also changed
v4 = np.zeros([3,3], dtype=str)
print('V3 with Zeros with str', v4)
'''
[
    [0, 0],
    [0, 0],
    [0, 0]
]
'''

v5 = np.ones([4, 2], dtype=int);
print('V5 = ', v5)
'''
[
    [1, 1],
    [1, 1],
    [1, 1]
    [1, 1]
]
'''

v6 = np.arange(9);
print('V6 =', v6) # [0, 1, 2, 3, 4, 5, 6, 7, 8]

v7 = np.arange(1, 9, 2);
print('v7', v7) # [1, 3, 5, 7]

# As Name suggest, - some random number of elements to be showed
# linspace(start(inclusion), end(inclusion), no_of_random_elements_to_be_present)
v8 = np.linspace(1, 10, 5, dtype=int);
print('V8', v8) # [1, 3, 6, 9, 10] - displayed 5 numbers

# Generating the random numbers
v9 = np.random.rand(3, 4);
# This will generate the random float numbers with matrix size [3 * 4]
print("V9 ", v9);

# Now randn - includes the -ve float integers
v10 = np.random.randn(3, 4);
print('V10', v10)

# Now randn - includes the integer integers
# randint(max_number_it_can_generate, size of the matix)
v11 = np.random.randint(5, size=(2,4));
print('V11', v11); 
'''
[[1, 3], [4, 2], [3, 1], [1, 5]], All the elements are actually generated with the limit which we set as the first argument
'''