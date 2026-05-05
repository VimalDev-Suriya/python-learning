
# *********** TypeCasting ****************
print("*********** TypeCasting ***********")
# if we want to change the tuple value, we can typecast from tuple to list
myTuple = ("hello", 1, 2);
convertedTupleToList = list(myTuple);
print(convertedTupleToList);

convertedTupleToList[0] = "changed";

myTuple = tuple(convertedTupleToList);
print(myTuple);

print(int("1"), type(int('101')));

print(bool("hello")); # true
print(bool(-1)); # true
print(bool(1)); # true
print(bool(0)); # false
print(bool([])); # false
print(bool(())); # false
print(bool({})); # false
print(bool(None)); # false

print("*********** TypeCasting ***********")