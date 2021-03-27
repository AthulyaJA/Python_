'''class Rectangle:
    def __init__(self,le,br):
        self.l=le
        self.b=br
        
    def get_area(self):
         return self.l*self.b
         
    def get_peri(self):
          return 2*(self.l+self.b)
          
le=int(input("enter the value"))
br=int(input("enter the second value"))
rect=Rectangle(le,br)
print("area=",rect.get_area())'''
class rectangle:
    def __init__(self,le,br):
         self.l=le
         self.b=br
    def get_area(self):
        peri=self.l*self.b
        return peri
           
    def get_peri(self):
        area=2*(self.l+self.b)
        return area


p=rectangle(3,2)
print("area=",p.get_area())
print("perimeter=",p.get_peri())
            

      