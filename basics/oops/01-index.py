# Class - collection of Objects
# Object - Instance of class

class Student:
    id = 110 # datamember of the class
    name = "Accenture" # datamember of the class

    # This is called as Class Method
    # "self" is the better was to name the "this" argument, grom where we can access the Class properties
    # ALWAYS the 1st param of class methods should always map to `self`
    def display(self, param1, param2):
        print("Self",self, self.id, self.name);
        print('Type of Self', type(self)) # <class '__main__.Student'>
        print('Params', param1, param2)

student1 = Student()
print("Student ID",student1.id)
print("Student Name",student1.name)
student1.display("1", "2");