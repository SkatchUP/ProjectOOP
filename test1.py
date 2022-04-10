class A:
    def hi(self):
        print("A")
 
class B(A):
    def hih(self):
        print("B")
 
class C(A):
    def hi(self):
        print("C")
 
class D(B, C):
    pass
 
# d = D()
# d.hi()
print(D.mro())