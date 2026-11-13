class Point:
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        
    def get_x(self):
        return self.x_coordinate
    def get_y(self):
        return self.y_coordinate
        
    def __str__(self):
        msg = ""
        msg += f"({self.get_x()}, {self.get_y()})"
        return msg
    
    def __add__(self, other):
        new_x = self.get_x() + other.get_x()
        new_y = self.get_y() + other.get_y()
        return Point(new_x, new_y)

p1 = Point(3,4)
p2 = Point(2,7)

p3 = p1 + p2
print(p3)  # Should print (5, 11)

p4 = Point(1, 1)

p5 = p3 + p4
print(p5)  # Should print (6, 12)

p6 = Point(3, 4)
print(p6)  # Should print (3, 4)

# is p1 equal to p2
print(p1 == p2)  # Should print False

# is p5 equal to p6
print(p5 == p6)  # Should print False