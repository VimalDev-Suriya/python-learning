# Heirarchical Inheritance
# Multiple mulilevel Instance 
# Consider this as the Tree a -> b & a -> c

class A:
    def fun_a(self):
        print('Root 1 class')

class B(A):
    def fun_b(self):
        print('Left Child 1 class')

class C(A):
    def fun_c(self):
        print('Right Child 1 class')


obj = C();
obj.fun_a();
obj.fun_c();

obj = B();
obj.fun_a();
obj.fun_b();