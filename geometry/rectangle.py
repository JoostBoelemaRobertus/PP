#we create __init__.py just to indicate that the package folder is a package, not 'necessary' just better to have

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def __str__(self):
        return "Rectangle: " + str(self.width) + " x " + str(self.height) + "; area: " + str(self.area())
    

rect = Rectangle(5, 20)
str(rect)