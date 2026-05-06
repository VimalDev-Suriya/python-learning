# Encapsulation are done by naming convention in python

# Type 1 - Public
class Student1:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name);

student_1 = Student1("Suriya");
student_1.get_name();
print(student_1.name);

# Type 2 - Protected
# Here we can access the Variables and functions declared with "Single underscore", as from python only for developers standpoint it was expected. But from functionality standpoint it is still public
class A:
    _a = "hello"

class Student2(A):
    _name = "surya"

    def _get_name(self):
        print("Protected",self._name)

student_2 = Student2();
student_2._get_name();
print("Protected",student_2._name);
print("Protected",student_2._a);

# Type 3 - Private
class Parent:
    __a = "hello"

class Student3(Parent):
    __name = "surya"

    def __get_name(self):
        print("Private", self.__name)
    
    def test(self):
        self.__get_name();

student_3 = Student3();
# print("Private Variable", student_3.__name) # this will throw error
# student_3.__get_name(); # This will throw error
# print("Private from parent", student_3.__a) # This will throw error
student_3.test()