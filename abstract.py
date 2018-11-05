# a public
# _a private --still accessible from outside
# __a strictly private --not accessible from outside (name )
class Person:
	def __init__(self,name):
		self.__name=name
	def getName(self):
		return self.__name

p=Person('jyo')
print(p.getName())
print(p.__name)
#distance between points and addition
from math import sqrt
class Point:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __add__(self,other):
        x=self.a+other.a
        y=self.b+other.b
        z=self.c+other.c
        return Point(x,y,z)

p1=Point(4,5,6)
p2=Point(-2,-1,4)
distance = sqrt( (p1.a-p2.a)**2 + (p1.b-p2.b)**2 + (p1.c -p2.c)**2 )
print(distance)
p3=p1+p2
print(p3.a,p3.b,p3.c)
#even odd
class TestIsEven:
    def __init__(self,a):
        self.a=a
    def isEven(self):
        if (self.a)%2 == 0:
            return True
        else: return False
t=TestIsEven(1121)
print(t.isEven())
