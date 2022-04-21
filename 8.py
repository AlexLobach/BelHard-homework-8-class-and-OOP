from math import sqrt
from abc import ABC, abstractmethod


class Point:
    def __init__(self, float_x, float_y,):
        self.float_x = float_x
        self.float_y = float_y
        self._length = Line (self.float_x, self.float_y)
        
    def length(self):
        return "Length = " + str(self._length.pythagor()) 

class Line:
    def __init__(self, float_x, float_y,):
        self.float_x = float_x
        self.float_y = float_y
          
    def pythagor(self):
        length = (sqrt(self.float_x**2 + self.float_y**2))
        return length #теорема Пифагора

class Shape(ABC):
    @abstractmethod
    def area (self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square (Line,Shape):
    def area(self):
        return "Area Square = " + str (sqrt(self.pythagor())**2)
    
    def perimeter(self):
        return "Perimeter Square = " + str (4 * self.pythagor())


class Rect (Shape):
    def __init__(self,float_x, float_y, side_b):
        self.float_x = float_x
        self.float_y = float_y
        self.side_b = side_b
        self.side_a = Line.pythagor(self)
        
    def area(self):
        return "Area Rect = " + str (self.side_b * self.side_a)
    
    def perimeter(self):
        return "Perimeter Rect = " + str (2 * self.side_a + self.side_b)


class Cube(Square):
    def volume (self):
        return "Volume Cube = " + str (sqrt(self.pythagor())**3)




point = Point (13,22)
rect = Rect(13,22,22)
squere = Square (13,22)
cube = Cube (13,22)
print (point.length (), squere.area(), squere.perimeter(), rect.area(), rect.perimeter(), cube.volume(), sep = "\n" )



 