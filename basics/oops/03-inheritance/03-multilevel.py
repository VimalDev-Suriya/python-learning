# Multilevel Inheritance
# Multiple SIngle level Instance 

class A:
    def fun_a(self):
        print('Grandparent 1 class')

class B(A):
    def fun_b(self):
        print('Parent 1 class')

class C(B):
    def fun_c(self):
        print('Child 1 class')


obj = C();
obj.fun_a();
obj.fun_b();
obj.fun_c();