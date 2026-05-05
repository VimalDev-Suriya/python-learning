
print("*********** Handling Exceptions ***********")
val_1 = int(input("Enter the input A = "))
val_2 = int(input("Enter the input B = "))

try:
    c = val_1 / val_2;
except Exception as e:
    print("Invalid input",e);
else:
    print('Else Block') # it will execute only if there is NO Error /Exception
finally:
    print('Finally Block') # Always run, clean up
print("*********** Handling Exceptions ***********")
