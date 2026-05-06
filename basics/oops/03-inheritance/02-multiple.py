class A:
    def fun_a(self):
        print('Base 1 class')

class B:
    def fun_b(self):
        print('Base 2 class')

# Multiple Inheritance
# B(A, B) is the syntax, where A's property can be derived or accessed by A's & B's instance
class C(A, B):
    def fun_c(self):
        print('Child class')


obj = C();
obj.fun_a();
obj.fun_b();
obj.fun_c();