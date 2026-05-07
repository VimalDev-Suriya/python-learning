import pandas as pd

employee_df = pd.read_csv(r"./basics/libraries/pandas-py/employee.csv")
print(employee_df);

print(employee_df.count()); # returns the number of items present in 

print('*' * 10)
print('Info')
print(employee_df.info())
print('*' * 10)

print('*' * 10)
print('Describe')
print(employee_df.describe())
print('*' * 10) 

print('*' * 10)
print('is Null')
print(employee_df.isnull())
print('*' * 10) 

print('*' * 10)
print('is Duplicated')
print(employee_df.duplicated())
print('*' * 10) 