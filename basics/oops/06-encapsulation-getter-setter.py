'''
# Below is the issue we can fix
class Student1:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name);

student_1 = Student1("Suriya");
student_1.get_name(); # Suriya
student_1.name = "Keerthana"
student_1.get_name(); # Keerthana
'''

# Below Code works, I can set & get the name
'''
class Student:
    def __init__(self, name):
        self.__name = name;

    def get_name(self):
        return self.__name;

    def set_name(self, new_name):
        self.__name = new_name;


student_1 = Student("Suriya");
print("Name",student_1.get_name());
student_1.set_name('Keerthana');
print("Name",student_1.get_name());
'''

class Student:
    def __init__(self, name):
        self.__name = name;

    @property # getter
    def name(self):
        return self.__name;

    @name.setter # setter - we can add validations and throw error
    def set_name(self, new_name):
        self.__name = new_name;


student_1 = Student("Suriya");
print(student_1.name); # Due to @property I can able to access like property, though it as defined as function
student_1.set_name = "Keerthana"
print(student_1.name)

'''
@property
- A Property which makes the method into the property - To access the private variables
- Without this we should 

@name.setter
- Once we create the method with @property, python will create a secodary directory with `.setter`
- Syntax - @<method_name_of_property>.setter
'''