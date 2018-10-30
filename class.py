class Sample:
    pass
my_sample = Sample()
print(type(my_sample))

class Dog():
    def __init__(self,category,name,spots):
        self.category = category
        self.name = name
        self.spots= spots
my_list = Dog(category='dog',name='kuper',spots='YES')
print(my_list.category)
print(my_list.name)
print(my_list.spots)

Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
class Line(object):
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)
coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())

Find volume and area of a cylinder
class Cylinder(object):
    def __init__(self, height = 1, radius = 1):

        self.height = height
        self.radius = radius

    def volume(self):

        return 3.14 * (self.radius)**2 * (self.height)

    def surface_area(self):

        return (2 * 3.14 * (self.radius) * (self.height) + 2 * 3.14 * (self.radius)**2)
        
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())


