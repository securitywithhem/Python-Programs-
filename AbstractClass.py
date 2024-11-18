'''23.Describe abstract class called Shape which has three subclasses say Triangle, Rectangle, Circle. Define one method area() 
in the abstract class and override this area() in these three subclasses to calculate for specific object i.e. area() of Triangle 
subclass should calculate area of triangle etc. Same for Rectangle and Circle'''
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*(self.radius**2)
base= int(input("Enter the base for triangle:"))
height= int(input("Enter the height for triangle:"))
length=int(input("Enter the length for rectangle:"))
breadth=int(input("Enter the breadth for rectangle:"))
radius=int(input("Enter the radius of the circle:"))
AreaTriangle=Triangle(base,height)
AreaRectangle=Rectangle(length,breadth)
AreaCircle=Circle(radius)
print(f"The area of triangle is: {AreaTriangle.area()}")
print(f"The area of rectangle is: {AreaRectangle.area()}")
print(f"The area of circle is: {AreaCircle.area()}")