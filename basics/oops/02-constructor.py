# Constructor are the built in function, which allocates the memory for the class
# It will be executed by default whenever we create the instance of the Object
# By default python will not support multi constructor
class Student:
    def __init__(self):
        print("I am Default constructor")
        print("Self", self);
        print("Type", type(self));

    # Below code will always be consider while creating the instance
    def __init__(self, param1, param2):
        print("I am Parametrized constructor")
        print("Self", self);
        print("Type", type(self));
        print('Params', param1, param2)

# Instance of the Student class
student_1 = Student("1", "2")