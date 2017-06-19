#Author: Cecelia Williams
#Last Revision: 04.29.2017
#Description: Chapter 16 Exercise 5


class Point:
    """ Point class represents and manipulates x,y coordinates. """

    def __init__(self, x, y):
        """ Create a new point at the origin. """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return((self.x ** 2) + (self.y ** 2)) ** 0.5

    def print_point(p):
        print("({0}, {1})".format(pt.x, pt.y))

    def to_string(self):
        return "({0}, {1})".format(self.x, self.y)

    


class Rectangle:
    """ A class to manufacture rectangular objects """

    def __init__(self, posn, w, h):
        """ Initilize rectangle at posn, with with w, height h """
        self.corner1 = posn
        self.corner2 = posn
        self.width = w
        self.height = h


    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner1,self.width, self.height)




#def do_they_intersect(big,lil):
    
    
    
big_box = Rectangle((-150,40), 100, 200)
lil_box = Rectangle((150,-20), 50, 100)

big_box.forward(50)

print("big box: ",big_box)
print("little box: ",lil_box)
