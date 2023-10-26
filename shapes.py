class Shape:
    def __init__(self,name):
        self.name = name

# method for area
    def calculate_area(self):
        pass  



class Circle(Shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius = radius
        

    def calculate_area(self):
        return   3.14*self.radius**2


class Rectangle(Shape):
    def __init__(self,name,length,width):
        super().__init__(name)
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length*self.width


class Triangle(Shape):
    def __init__(self,name,base,height):
        super().__init__(name)
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5*self.base*self.height


circle =Circle("circle",4)
rectangle =Rectangle("rectangle",7,8)
triangle =Triangle("triangle",3,8)

shapes = [rectangle,triangle,circle]


for shapes in shapes:
    area = shapes.calculate_area()
    print(f"Name:{shapes.name} \n area:{area:.2f}")    