'''class my_name:
    name="athulya"
    def display(self):
        print("hello")
p=my_name()
print(p.name)
p.display()'''
'''class my_class:
    def __init__(b,name,age):
        b.n=name
        b.a=age
p=my_class("john","36")
print(p.a)
print(p.n)'''
"""class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def my_function(self):
        print("my name is :",self.name)
p=person("athulya",56)
p.my_function()"""

class car:
    def __init__(self,m,col,s):
        self.model=m
        self.color=col
        self.speed=s
    def my_car(self):
        print("my car color is :",self.color)
        print("my car model is :",self.model)
        print("my car speed is :",self.speed)
        
maruthy=car("800","red","200")
duster=car("4","black","500")
maruthy.my_car()
duster.my_car()
'''print(maruthy.speed)
print(maruthy.model)
print(maruthy.color)'''
        

    