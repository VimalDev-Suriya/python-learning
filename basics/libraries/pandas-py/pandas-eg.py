import pandas as pd;

# Used to create the table or dataset from the list
s1 = pd.Series([1, 2, 3, 4, 5])
print("S1 using list alone", s1)

s2 = pd.Series({"id": 1, "Name": "Suriya", "Age": 29})
print("S2")
print(s2)

df = pd.DataFrame([[101, "Planet A"], [102, "Planet B"], [103, "Planet C"]])
print("Data frame - Default")
print(df); # The rows and column label will be defaulted by indexes like 0,1...

# We can explicity set the labels of rows and columsn as
# columns is for labeling the columns
# index is for the labelling teh rows
df1 = pd.DataFrame([[101, "Planet A"], [102, "Planet B"], [103, "Planet C"]], columns=["Id", "Planet-Name"], index=["a", "b", "c"])
print(df1)