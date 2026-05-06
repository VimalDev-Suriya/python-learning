'''
Inhetitance:

1. Single Inheritance - 1 base, 1 child
2. Multiple Inheritance - Multiple Base and 1 child
3. Multi Level
4. Heirarchical
'''

class A:
    def fun_a(self):
        print('Base class')

# Single Inheritance
# B(A) is the syntax, where A's property can be derived or accessed by B's instance
class B(A):
    def fun_b(self):
        print('Child class')

obj = B();
obj.fun_a();
obj.fun_b();