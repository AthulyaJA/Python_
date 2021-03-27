# single line inheritance
"""class parent:
    def first(self):
        print("hello")
class child(parent):
    def second(self):
        print("hai")
obj=child()
obj.first()
obj.second()"""
# multiline
"""class perent1:
    def first(self):
        print("heloo")
class perent2:
    def second(self):
        print("hai")
class child(perent1,perent2):
    def third(self):
        print("welcome")
d=child()
d.first()
d.second()"""
# multilevel
"""class perent:
    def first(self):
        print("hai")
class child(perent):
    def second(self):
        print("heloo")
class Grandchild(child):
    def third(self):
        print("welcome")
d=Grandchild()
d.first()
d.second()
d.third()"""
# hirecheal inheritane
"""class A:
    def first(self):
        print("hai")
class B(A):
    def second(self):
        print("hello")
class C(A):
    def third(self):
        print("welcome")
d=C()
m=B()
d.first()
m.second()
m.first()
d.third()"""
#hybrid
"""class perent1:
    def first(self):
        print("hello")
class child1(perent1):
    def second(self):
        print("hai")
class child2(perent1):
    def third(self):
        print("welcome")
class child3(child1,child2):
    def fourth(self):
        print("sorry")
d=child3()
m=child1()
d.second()
d.third()
m.first()
d.fourth()"""
#pass :it is used to  passing the value from perent class to child class
'''f=input("enter the word:")
l=input("enter the second word")
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def show(self):
        print(self.firstname,self.lastname)
        print("first name:",self.firstname)
        print("last name:",self.lastname)
class student(person):
    pass
x=student(f,l)
x.show()'''
# mehod overloading
'''class overloading:
    def display(self,a=None,b=None):
        print(a,b)
obj=overloading()
obj.display(10,20)'''
# metthod overriding
'''class father:
    def trans(self):
        print("cycle")
class son(father):
    def trans(self):
        print("bike")
d=son()
#b=father()
#b.trans()
d.trans()'''
#python to find count the occurance of a given word in a sring sentance
a=input("enter the word:")
b="athu"
count = a.count(b)
print(count)   
    


    